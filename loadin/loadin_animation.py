from sys import stdout as out
from collections import deque
import itertools
import time


def simple_ui(_cycle_str, _str, _speed):
    for i in itertools.cycle(_cycle_str):
        status = '{} {} '.format(_str, i)
        out.write(status)
        out.flush()
        out.write('\x08' * len(status))
        time.sleep(_speed)


def long_ui(_cycle_str, _str, _speed):
    _cycle_list = deque(_cycle_str)
    while True:
        status = '{} {}'.format(_str, ''.join(_cycle_list))
        out.write(status)
        out.flush()
        out.write('\x08'*len(status))
        _cycle_list.appendleft(_cycle_list.pop())
        time.sleep(_speed)


def cycle_ui(_str, _speed):
    simple_ui('|/-\\', _str, _speed)


def point_ui(_str, _speed):
    simple_ui(('.  ', '.. ', '...'), _str, _speed)


def wave_ui(_str, _speed):
    long_ui(('▁▂▃▅▆▇▆▅▃▂▁'), _str, _speed)


STYLE_DICT = {
    'cycle': cycle_ui,
    'point': point_ui,
    'wave': wave_ui
}
