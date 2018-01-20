from sys import stdout as out
import itertools
import time

CYCLE_TIME = 0.2


def base_ui(_cycle_str, _str):
    for i in itertools.cycle(_cycle_str):
        status = '{} {} '.format(_str, i)
        out.write(status)
        out.flush()
        out.write('\x08' * len(status))
        time.sleep(CYCLE_TIME)


def cycle_ui(_str):
    base_ui('|/-\\', _str)


def point_ui(_str):
    base_ui(('.  ', '.. ', '...'), _str)


STYLE_DICT = {
    'cycle': cycle_ui,
    'point': point_ui,
}
