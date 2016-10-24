#!/usr/bin/env python3
#   encoding: utf8
#   test.py

from tskv import *


def test_load():
    in1 = 'tskv\tk1=v1\tk2=v2'
    out1 = dict(k1='v1', k2='v2')

    assert out1 == load(in1)

def test_dump():
    in1 = dict(k1='v1', k2='v2')
    out1 = 'tskv\tk1=v1\tk2=v2'

def test_quote():
    value_in = '\\tes\tst\ri\ng==\0'
    value_out = quote(value_in)

    assert value_out == '\\\\tes\\tst\\ri\\ng\\=\\=\\0'

def test_unquote():
    value_in = '\\\\tes\\tst\\ri\\ng\\=\\=\\0'
    value_out = unquote(value_in)

    assert value_out == '\\tes\tst\ri\ng==\0'

def test():
    test_dump()
    test_load()
    test_quote()
    test_unquote()


if __name__ == '__main__':
    test()
