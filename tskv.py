#   encoding: utf8
#   tskv.py

from itertools import takewhile

__all__ = (
    'dump',
    'load',
    'quote',
    'unquote',
)

TSKV_PREFIX = 'tskv'


def dump(rec):
    parts = [TSKV_PREFIX]

    for key, val in rec.items():
        parts.append('='.join((quote(key), quote(val))))

    row = '\t'.join(parts)

    return row

def load(raw):
    if not raw.startswith(TSKV_PREFIX + '\t'):
        raise ValueError('Raw content is not in TSKV format: '
                         'it should start with `tskv\\t`.')

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
    return (value.
            replace('=', '\\=').
            encode('unicode_escape').
            decode('ascii'))

def unquote(value):
    return (value.
            encode('ascii').
            decode('unicode_escape').
            replace('\\=', '='))
