# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
from pygal.util import (
    round_to_int, round_to_float, _swap_curly, template, humanize)
from pytest import raises


def test_round_to_int():
    assert round_to_int(154231, 1000) == 154000
    assert round_to_int(154231, 10) == 154230
    assert round_to_int(154231, 100000) == 200000
    assert round_to_int(154231, 50000) == 150000
    assert round_to_int(154231, 500) == 154000
    assert round_to_int(154231, 200) == 154200
    assert round_to_int(154361, 200) == 154400


def test_round_to_float():
    assert round_to_float(12.01934, .01) == 12.02
    assert round_to_float(12.01134, .01) == 12.01
    assert round_to_float(12.1934, .1) == 12.2
    assert round_to_float(12.1134, .1) == 12.1
    assert round_to_float(12.1134, .001) == 12.113
    assert round_to_float(12.1134, .00001) == 12.1134
    assert round_to_float(12.1934, .5) == 12.0
    assert round_to_float(12.2934, .5) == 12.5


def test_swap_curly():
    for str in (
            'foo',
            u'foo foo foo bar',
            'foo béè b¡ð/ĳə˘©þß®~¯æ',
            u'foo béè b¡ð/ĳə˘©þß®~¯æ'):
        assert _swap_curly(str) == str
    assert _swap_curly('foo{bar}baz') == 'foo{{bar}}baz'
    assert _swap_curly('foo{{bar}}baz') == 'foo{bar}baz'
    assert _swap_curly('{foo}{{bar}}{baz}') == '{{foo}}{bar}{{baz}}'
    assert _swap_curly('{foo}{{{bar}}}{baz}') == '{{foo}}{{{bar}}}{{baz}}'
    assert _swap_curly('foo{ bar }baz') == 'foo{{ bar }}baz'
    assert _swap_curly('foo{ bar}baz') == 'foo{{ bar}}baz'
    assert _swap_curly('foo{bar }baz') == 'foo{{bar }}baz'
    assert _swap_curly('foo{{ bar }}baz') == 'foo{bar}baz'
    assert _swap_curly('foo{{bar }}baz') == 'foo{bar}baz'
    assert _swap_curly('foo{{ bar}}baz') == 'foo{bar}baz'


def test_format():
    assert template('foo {{ baz }}', baz='bar') == 'foo bar'
    with raises(KeyError):
        assert template('foo {{ baz }}') == 'foo baz'

    class Object(object):
        pass
    obj = Object()
    obj.a = 1
    obj.b = True
    obj.c = '3'
    assert template('foo {{ o.a }} {{o.b}}-{{o.c}}',
               o=obj) == 'foo 1 True-3'


def test_humanize():
    assert humanize(1) == '1'
    assert humanize(10) == '10'
    assert humanize(12.5) == '12.5'
    assert humanize(1000) == '1k'
    assert humanize(5000) == '5k'
    assert humanize(100000) == '100k'
    assert humanize(1253) == '1.253k'
    assert humanize(1250) == '1.25k'

    assert humanize(0.1) == '100m'
    assert humanize(0.01) == '10m'
    assert humanize(0.001) == '1m'
    assert humanize(0.002) == '2m'
    assert humanize(0.0025) == '2.5m'
    assert humanize(0.0001) == u'100µ'
    assert humanize(0.000123) == u'123µ'
    assert humanize(0.00001) == u'10µ'
    assert humanize(0.000001) == u'1µ'
    assert humanize(0.0000001) == u'100n'
    assert humanize(0.0000000001) == u'100p'

    assert humanize(0) == '0'
    assert humanize(-1337) == '-1.337k'
    assert humanize(-.000000042) == '-42n'
