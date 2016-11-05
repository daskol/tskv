#!/usr/bin/env python3
#   encoding: utf8
#   test.py

import unittest

from os import fdopen, unlink
from tempfile import mkstemp
from tskv import *


class TskvTest(unittest.TestCase):

    def test_load(self):
        in1 = 'tskv\tk1=v1\tk2=v2'
        out1 = dict(k1='v1', k2='v2')

        fd, name = mkstemp(text=True)

        with fdopen(fd, 'w') as fout:
            fout.write(in1)
            fout.write('\n')

        with open(name, 'r') as fin:
            assert out1 == load(fin)

        unlink(name)

    def test_loads(self):
        in1 = 'tskv\tk1=v1\tk2=v2'
        out1 = dict(k1='v1', k2='v2')

        assert out1 == loads(in1)

    def test_dump(self):
        in1 = dict(k1='v1', k2='v2')
        out1a = 'tskv\tk1=v1\tk2=v2\n'
        out1b = 'tskv\tk2=v2\tk1=v1\n'

        fd, name = mkstemp(text=True)

        with fdopen(fd, 'w') as fout:
            dump(in1, fout)

        with open(name, 'r') as fin:
            data = fin.read()

            assert any([
                out1a == data,
                out1b == data,
            ])

        unlink(name)

    def test_dumps(self):
        in1 = dict(k1='v1', k2='v2')
        out1a = 'tskv\tk1=v1\tk2=v2'
        out1b = 'tskv\tk2=v2\tk1=v1'

        assert any([
            out1a == dumps(in1),
            out1b == dumps(in1),
        ])

    def test_quote(self):
        value_in = '\\tes\tst\ri\ng==\0'
        value_out = quote(value_in)

        assert value_out == '\\\\tes\\tst\\ri\\ng\\\\=\\\\=\\x00'

    def test_unquote(self):
        value_in = '\\\\tes\\tst\\ri\\ng\\=\\=\\0'
        value_out = unquote(value_in)

        assert value_out == '\\tes\tst\ri\ng==\0'


if __name__ == '__main__':
    unittest.main()
