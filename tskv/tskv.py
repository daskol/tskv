#   encoding: utf8
#   tskv.py

from io import TextIOBase
from itertools import takewhile

__all__ = (
    'dump',
    'dumps',
    'load',
    'loads',
    'quote',
    'unquote',
)

TSKV_PREFIX = 'tskv'


def dump(obj, fp):
    if not isinstance(fp, TextIOBase):
        raise ValueError('File-like object should be instance of TextIOBase')

    row = dumps(obj)

    fp.write(row)
    fp.write('\n')

def dumps(rec):
    parts = [TSKV_PREFIX]

    for key, val in rec.items():
        parts.append('='.join((quote(key), quote(val))))

    row = '\t'.join(parts)

    return row

def load(fp):
    if not isinstance(fp, TextIOBase):
        raise ValueError('File-like object should be instance of TextIOBase')

    line = fp.readline()
    record = loads(line)
    return record

def loads(raw):
    if not raw.startswith(TSKV_PREFIX + '\t'):
        raise ValueError('Raw content is not in TSKV format: '
                         'it should start with `tskv\\t`.')

    if raw[-1] == '\n':
        raw = raw[:-1]

    record = dict()
    kv_pairs = raw[5:].split('\t')

    for pair in kv_pairs:
        if not pair:
            ValueError('Raw content is not in TSKV format: '
                       'it contains too many tab separators.')

        parts = pair.split('=')
        prefix = tuple(takewhile(lambda x: x.endswith('/'), parts))
        key = '='.join(parts[:len(prefix) + 1])
        val = '='.join(parts[len(prefix) + 1:])
        record[unquote(key)] = unquote(val)

    return record

def quote(value):
    return (str(value).
            replace('=', '\\=').
            encode('unicode_escape').
            decode('ascii'))

def unquote(value):
    return cast((value.
            encode('ascii').
            decode('unicode_escape').
            replace('\\=', '=')))

def boolean(value):
    if value == 'False':
        return False
    elif value == 'True':
        return True
    else:
        raise ValueError('Value is not type of bool.')

def none(value):
    if value:
        raise ValueError('Value is not None type.')
    else:
        return None

def cast(value):
    cast_operators = (
        int,
        float,
        boolean,
        none,
    )

    for operator in cast_operators:
        try:
            return operator(value)
        except ValueError:
            continue

    return value
