import sys
import itertools
import time


def cycle_ui(_str):
    for i in itertools.cycle('|/-\\'):
        status = '{} {}'.format(_str, i)
        sys.stdout.write(status)
        sys.stdout.flush()
        sys.stdout.write('\x08' * len(status))
        time.sleep(.2)


def point_ui(_str):
    for i in itertools.cycle(('.', '..', '...')):
        status = '{} {}'.format(_str, i)
        sys.stdout.write(status)
        sys.stdout.flush()
        sys.stdout.write('\x08' * len(status))
        time.sleep(.2)


STYLE_DICT = {
    'cycle': cycle_ui,
    'point': point_ui,
}
