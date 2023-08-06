"""A data wrangling tool which requires no knowledge of Pandas or SQL.
"""

import os
import signal
import sqlite3
import tempfile
from collections import deque
from contextlib import contextmanager
from copy import copy
from itertools import (chain, dropwhile, groupby, islice, product, takewhile,
                       zip_longest)
from pathlib import Path, PurePath


class Conn:
    """Connection to a SQL database file.

    Example:
        conn = Conn('sample.db')
    """

    def __init__(self, dbfile):
        # dbfile must be a filename(str), can't be :memory:
        if PurePath(dbfile).is_absolute():
            self._dbfile = dbfile
        else:
            self._dbfile = os.path.join(os.getcwd(), dbfile)

        self._dbconn = None

    def __getitem__(self, tname):
        return Rows((self, tname))

    def __setitem__(self, tname, val):
        with _connect(self._dbfile) as c:
            self._dbconn = c
            _delete(c, tname)
            _insert(c, tname, _rows2iter(val))


class Rows:
    """
    """

    def __init__(self, src):
        if isinstance(src, tuple):
            conn, tname = src

            self._src = src
            self._history = [{
                'cmd': 'fetch',
                'conn': conn,
                'tname': tname,
                'genfn': _build_initgen(conn, tname, [])

            }]

        else:
            self._src = list(src)

            def gen():
                yield from self._src

            self._history = [{
                'cmd': 'read',
                'genfn': gen
            }]

    def __str__(self):
        return "\n".join(str(r) for r in self._iter())

    def __getitem__(self, col):
        return [r[col] for r in self._iter()]

    def zip(self, other):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen1():
            for r1, r2 in zip(pgen(), _rows2iter(other)):
                yield {**r1, **r2}

        # if the source is the database, it's safe to update rows directly
        # because tablemap creates new rows every time you iterate rows
        def gen2():
            for r1, r2 in zip(pgen(), _rows2iter(other)):
                r1.update(r2)
                yield r1

        # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'zip',
            'genfn': gen2 if self._history[0]['cmd'] == 'fetch' else gen1
        }]

        return newself

    def zip_longest(self, other):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen1():
            r1, rs1 = _spy(pgen())
            r2, rs2 = _spy(_rows2iter(other))
            empty1 = {col: '' for col in r1.keys()}
            empty2 = {col: '' for col in r2.keys()}

            for r1, r2 in zip_longest(rs1, rs2):
                if r1 and r2:
                    yield {**r1, **r2}
                elif r1 and not r2:
                    yield {**r1, **empty2}
                elif not r1 and r2:
                    yield {**empty1, **r2}

        def gen2():
            r1, rs1 = _spy(pgen())
            r2, rs2 = _spy(_rows2iter(other))
            # using the same object over and over is SAFE
            empty1 = {col: '' for col in r1.keys()}
            empty2 = {col: '' for col in r2.keys()}

            for r1, r2 in zip_longest(rs1, rs2):
                if r1 and r2:
                    r1.update(r2)
                    yield r1
                elif r1 and not r2:
                    r1.update(empty2)
                    yield r1
                elif not r1 and r2:
                    empty1.update(r2)
                    yield empty1

        # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'zip_longest',
            'genfn': gen2 if self._history[0]['cmd'] == 'fetch' else gen1
        }]
        return newself

    def chain(self, other):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen():
            for r in pgen():
                yield r
            for r in _rows2iter(other):
                yield r

        newself._history = newself._history + [{
            'cmd': 'chain',
            'genfn': gen
        }]
        return newself

    # each column may contain asc or desc
    # ex) 'col1 desc', 'col2 asc'
    def order(self, *cols):
        newself = copy(self)
        if len(newself._history) == 1\
                and newself._history[-1]['cmd'] == 'fetch':
            phist = newself._history[-1]
            newself._history = [{
                **phist,
                'genfn': _build_initgen(phist['conn'], phist['tname'], cols)
            }]
            return newself

        pgen = newself._history[-1]['genfn']

        def gen_from_sql():
            try:
                tmpdbfd, tmpdb = tempfile.mkstemp()
                with _connect(tmpdb) as c:
                    _insert(c, 'temp', pgen())
                    yield from _fetch(c, 'temp', cols)
            # TODO: possible errors must be dealt with.
            finally:
                # must close the file descriptor to delete it
                os.close(tmpdbfd)
                if Path(tmpdb).is_file():
                    os.remove(tmpdb)

        def gen_simp():
            xs = list(pgen())
            # multiple column sorting needs an idea.
            for col in reversed(cols):
                rev = False
                cs = col.split()
                if len(cs) == 2:
                    c, desc = cs
                    if desc.lower() == 'desc':
                        rev = True
                else:
                    c = cs[0]
                xs.sort(key=lambda r: r[c], reverse=rev)
            yield from xs

        # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'order',
            'cols': cols,
            'genfn': gen_from_sql if newself._history[0]['cmd'] == 'fetch'
            else gen_simp
        }]

        return newself

    # End-users might not be able to pass proper functions.
    def _apply(self, fn):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen_single():
            for r in pgen():
                yield from fn(r)

        def gen_group():
            for k, rs in pgen():
                yield from fn(k, rs)

        def gen_windowed():
            for rs in pgen():
                yield from fn(rs)

        genfn = None
        if newself._history[-1]['cmd'] == 'group':
            genfn = gen_group
        elif newself._history[-1]['cmd'] == 'windowed':
            genfn = gen_windowed
        else:
            genfn = gen_single

        # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'apply',
            'genfn': genfn
        }]
        return newself

    def group(self, *cols):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen():
            yield from groupby(pgen(), _keyfn(cols))

         # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'group',
            'cols': cols,
            'genfn': gen
        }]

        return newself

    # TODO: not sure 'join' can completely replace this one.
    def _merge(self, fn, other):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen():
            yield from _step(fn, pgen(), _rows2iter(other))

         # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': '_merge',
            'genfn': gen
        }]

        return newself

    def map(self, fn):
        if self._history[-1]['cmd'] == 'group':
            def _fn2gen(f):
                def gen(_k, rs):
                    x = f(Rows(rs))

                    if isinstance(x, dict):
                        yield x
                    elif isinstance(x, Rows):
                        yield from x._iter()
                return gen
            return self._apply(_fn2gen(fn))

        elif self._history[-1]['cmd'] == 'windowed':
            def _fn2gen1(f):
                def gen(rs):
                    x = f(Rows(rs))
                    if isinstance(x, dict):
                        yield x
                    elif isinstance(x, Rows):
                        yield from x._iter()
                return gen

            return self._apply(_fn2gen1(fn))

        # single row
        def _fn2gen_single(f):
            def gen(r):
                x = f(r)
                if isinstance(x, dict):
                    yield x
                elif isinstance(x, Rows):
                    yield from x._iter()
            return gen
        return self._apply(_fn2gen_single(fn))

    def by(self, *cols):
        # need to cut out 'desc', 'asc'
        cols_for_group = [col.split()[0] for col in cols]
        return self.order(*cols).group(*cols_for_group)

    def filter(self, pred):
        def gen(r):
            if pred(r):
                yield r

        return self._apply(gen)

    def update(self, **kwargs):
        def updatefn1(r):
            d = r.copy()
            for k, v in kwargs.items():
                d[k] = v(d) if callable(v) else v
            yield d

        def updatefn2(r):
            for k, v in kwargs.items():
                r[k] = v(r) if callable(v) else v
            yield r

        if self._history[0]['cmd'] == 'fetch':
            return self._apply(updatefn2)
        return self._apply(updatefn1)

    # pretty expensive for what it actually does
    # but this version does not depend on the order of rows.
    def rename(self, **kwargs):
        kwargs_rev = {oldkey: newkey for newkey, oldkey in kwargs.items()}

        def renamefn(r):
            yield {kwargs_rev.get(oldkey, oldkey): v
                   for oldkey, v in r.items()}

        return self._apply(renamefn)

    def fold(self, **kwargs):
        gcols = []
        if self._history[-1]['cmd'] == 'group':
            gcols = self._history[-1]['cols']

        def foldfn1(rs):
            rs = Rows(rs)
            r = {}
            for k, fn in kwargs.items():
                r[k] = fn(rs) if callable(fn) else fn
            yield r

        def foldfn2(keys, rs):
            rs = Rows(rs)
            r = dict(zip(gcols, keys))
            for k, fn in kwargs.items():
                r[k] = fn(rs) if callable(fn) else fn
            yield r

        if self._history[-1]['cmd'] == 'windowed':
            return self._apply(foldfn1)
        if self._history[-1]['cmd'] == 'group':
            return self._apply(foldfn2)
        raise ValueError("fold must be preceded by grouping processes")

    def select(self, *cols):
        def selectfn(r):
            yield {col: r[col] for col in cols}

        return self._apply(selectfn)

    def deselect(self, *cols):
        cols = set(cols)

        def deselectfn(r):
            yield {k: v for k, v in r.items() if k not in cols}

        return self._apply(deselectfn)

    def join(self, other, join_type="left"):
        if join_type.lower() == "inner":
            return self._inner_join(other)
        elif join_type.lower() == "left":
            return self._left_join(other)
        elif join_type.lower() == "right":
            return self._right_join(other)
        elif join_type.lower() == "full":
            return self._full_join(other)
        raise ValueError("Unknown join_type", join_type)

    def _inner_join(self, other):
        def innerjoin_fn1(rs1, rs2, _left, _right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    r1.update(r2)
                    yield r1

        def innerjoin_fn2(rs1, rs2, _left, _right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    yield {**r1, **r2}

        if self._history[0]['cmd'] == 'fetch':
            return self._merge(innerjoin_fn1, other)
        return self._merge(innerjoin_fn2, other)

    def _left_join(self, other):
        def leftjoin_fn1(rs1, rs2, _left, right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    r1.update(r2)
                    yield r1

            elif rs1 != [] and rs2 == []:
                for r1 in rs1:
                    r1.update((col, '') for col in right_only)
                    yield r1

        def leftjoin_fn2(rs1, rs2, _left, right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    yield {**r1, **r2}

            elif rs1 != [] and rs2 == []:
                for r1 in rs1:
                    yield {**r1, **{col: '' for col in right_only}}

        if self._history[0]['cmd'] == 'fetch':
            return self._merge(leftjoin_fn1, other)
        return self._merge(leftjoin_fn2, other)

    def _right_join(self, other):
        def rightjoin_fn1(rs1, rs2, left, _right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    r1.update(r2)
                    yield r1

            elif rs1 == [] and rs2 != []:
                empty_left = {col: '' for col in left}
                for r2 in rs2:
                    empty_left.update(r2)
                    yield empty_left

        def rightjoin_fn2(rs1, rs2, left, _right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    yield {**r1, **r2}

            elif rs1 == [] and rs2 != []:
                for r2 in rs2:
                    yield {**{col: '' for col in left}, **r2}

        if self._history[0]['cmd'] == 'fetch':
            return self._merge(rightjoin_fn1, other)
        return self._merge(rightjoin_fn2, other)

    def _full_join(self, other):
        def fulljoin_fn1(rs1, rs2, left, right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    # TODO: updating on the same object multiple times.
                    # Still, why works?!!,
                    # yielding and returning a appended list is different.
                    # later modifications do not affect previous yielded object
                    # So anyway, these updates in all joining methods
                    # are perfectly safe.
                    r1.update(r2)
                    yield r1

            elif rs1 != [] and rs2 == []:
                for r1 in rs1:
                    r1.update((col, '') for col in right_only)
                    yield r1

            elif rs1 == [] and rs2 != []:
                empty_left = {col: '' for col in left}
                for r2 in rs2:
                    empty_left.update(r2)
                    yield empty_left

        def fulljoin_fn2(rs1, rs2, left, right_only):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    yield {**r1, **r2}

            elif rs1 != [] and rs2 == []:
                for r1 in rs1:
                    yield {**r1, **{col: '' for col in right_only}}

            elif rs1 == [] and rs2 != []:
                for r2 in rs2:
                    yield {**{col: '' for col in left}, **r2}

        if self._history[0]['cmd'] == 'fetch':
            return self._merge(fulljoin_fn1, other)
        return self._merge(fulljoin_fn2, other)

    def distinct(self, *columns):
        def distinctfn(_k, rs):
            yield next(rs)

        return self.by(*columns)._apply(distinctfn)

    def windowed(self, n, step):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen():
            yield from _windowed(pgen(), n, step)

         # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'windowed',
            'n': n,
            'step': step,
            'genfn': gen
        }]
        return newself

    def islice(self, *args):
        newself = copy(self)
        pgen = self._history[-1]['genfn']

        def gen():
            yield from islice(pgen(), *args)

         # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'islice',
            'args': args,
            'genfn': gen
        }]
        return newself

    def takewhile(self, pred):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen():
            yield from takewhile(pred, pgen())

        # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'takewhile',
            'genfn': gen
        }]
        return newself

    def dropwhile(self, pred):
        newself = copy(self)
        pgen = newself._history[-1]['genfn']

        def gen():
            yield from dropwhile(pred, pgen())

        # Do not use += operator here, it modifies the object
        newself._history = newself._history + [{
            'cmd': 'dropwhile',
            'genfn': gen
        }]
        return newself

    def size(self):
        # There are rooms for this to be more efficient because some of the
        # methods do not affect the size of the Rows but 
        # don't think it's worth the trouble.
        if len(self._history) == 1 and self._history[0]['cmd'] == 'fetch':
            origin = self._history[0]
            return _get_size(origin['conn'], origin['tname'])
        elif len(self._history) == 1 and self._history[0]['cmd'] == 'read':
            return len(self._src)
        return sum(1 for _ in self._iter())

    # iter is not safe to end-users, because the generator might not be
    # terminated after the database connection is closed.
    # This should be used in a controlled manner.
    def _iter(self):
        yield from self._history[-1]['genfn']()

    # list is safe, because it completes the iteration.
    def list(self):
        return list(self._iter())


def _insert_statement(name, d):
    """insert into foo values (:a, :b, :c, ...)

    Notice the colons.
    """
    keycols = ', '.join(":" + c.strip() for c in d)
    return f"insert into {name} values ({keycols})"


def _create_statement(tname, cols):
    """Create table if not exists foo (...)

    Note:
        Every type is numeric.
    """
    schema = ', '.join([col + ' ' + 'numeric' for col in cols])
    return f"create table if not exists {tname} ({schema})"


def _dict_factory(cursor, row):
    return {col[0]: val for col, val in zip(cursor.description, row)}


def _keyfn(cols):
    if len(cols) == 1:
        col = cols[0]
        return lambda r: r[col]
    return lambda r: [r[col] for col in cols]


def _delete(c, tname):
    c.cursor().execute(f'drop table if exists {tname}')


def _insert(c, tname, rs):
    rs = iter(rs)
    try:
        r0 = next(rs)
    except StopIteration:
        raise ValueError(f"No row to insert in {tname}") from None
    else:
        cols = list(r0)

        c.cursor().execute(_create_statement(tname, cols))
        istmt = _insert_statement(tname, r0)
        c.cursor().executemany(istmt, chain([r0], rs))


def _fetch(c, tname, cols):
    if cols:
        query = f"select * from {tname} order by {','.join(cols)}"
    else:
        query = f"select * from {tname}"

    yield from c.cursor().execute(query)


def _spy(it):
    val = next(it)
    return val, chain([val], it)


def _step(fn, krs1, krs2):
    empty = object()
    try:

        k1, rs1 = next(krs1)
        k2, rs2 = next(krs2)

        r1, rs1 = _spy(rs1)
        r2, rs2 = _spy(rs2)

        left = list(r1)
        right_only = [c for c in list(r2) if c not in list(r1)]

        while True:
            if k1 == k2:
                yield from fn(rs1, rs2, left, right_only)
                k1 = k2 = empty
                k1, rs1 = next(krs1)
                k2, rs2 = next(krs2)
            elif k1 < k2:
                yield from fn(rs1, [], left, right_only)
                k1 = empty
                k1, rs1 = next(krs1)
            else:
                yield from fn([], rs2, left, right_only)
                k2 = empty
                k2, rs2 = next(krs2)

    except StopIteration:
        # unconsumed
        if k1 is not empty:
            yield from fn(rs1, [], left, right_only)
        if k2 is not empty:
            yield from fn([], rs2, left, right_only)

        for _, rs1 in krs1:
            yield from fn(rs1, [], left, right_only)
        for _, rs2 in krs2:
            yield from fn([], rs2, left, right_only)


def _rows2iter(obj):
    return obj._iter() if isinstance(obj, Rows) else iter(obj)


def _build_initgen(conn, tname, cols):
    def initgen():
        try:
            yield from _fetch(conn._dbconn, tname, cols)
        # in case conn._dbconn is either None or closed connection
        except (AttributeError, sqlite3.ProgrammingError):
            with _connect(conn._dbfile) as c:
                conn._dbconn = c
                yield from _fetch(c, tname, cols)
    return initgen


def _get_size(conn, tname):
    try:
        res = conn._dbconn.cursor().execute(f"select count(1) from {tname}")
        return res.fetchone()['count(1)']
    except (AttributeError, sqlite3.ProgrammingError):
        with _connect(conn._dbfile) as c:
            res = c.cursor().execute(f"select count(1) from {tname}")
            return res.fetchone()['count(1)']


def _windowed(seq, n, step):
    if n < 0:
        raise ValueError('n must be >= 0')
    if n == 0:
        yield []
        return
    if step < 1:
        raise ValueError('step must be >= 1')

    window = deque(maxlen=n)
    i = n
    for _ in map(window.append, seq):
        i -= 1
        if not i:
            i = step
            yield list(window)

    size = len(window)
    if size == 0:
        return
    if size < n:
        yield list(window)
    elif 0 < i < min(step, n):
        yield list(window)[i:]


@contextmanager
def _connect(db):
    conn = sqlite3.connect(db)
    conn.row_factory = _dict_factory
    try:
        yield conn
    finally:
        # If users enter ctrl-c during the database commit,
        # db might be corrupted. (won't work anymore)
        with _delayed_keyboard_interrupts():
            conn.commit()
            conn.close()


@contextmanager
def _delayed_keyboard_interrupts():
    signal_received = []

    def handler(sig, frame):
        nonlocal signal_received
        signal_received = (sig, frame)
    # Do nothing but recording something has happened.
    old_handler = signal.signal(signal.SIGINT, handler)

    try:
        yield
    finally:
        # signal handler back to the original one.
        signal.signal(signal.SIGINT, old_handler)
        if signal_received:
            # do the delayed work
            old_handler(*signal_received)
