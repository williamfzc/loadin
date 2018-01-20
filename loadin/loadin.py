import multiprocessing
import sys
from .loadin_animation import STYLE_DICT


def start_loadin(style, tips):
    if not (isinstance(style, str) and isinstance(tips, str)):
        raise TypeError('Style and tips must be str.')
    if style not in STYLE_DICT:
        raise KeyError('Style {} not support.'.format(style))

    ui_process = multiprocessing.Process(
        target=STYLE_DICT[style],
        args=(tips,)
    )
    ui_process.start()
    return ui_process


def end_loadin(_proc):
    if _proc.is_alive():
        _proc.terminate()
    sys.stdout.write('\n')
    sys.stdout.flush()


def loading(style=None, tips=None):
    tips += ' '

    def inner(func):
        def _inner(*args, **kwargs):
            _process = start_loadin(style, tips)
            result = func(*args, **kwargs)
            end_loadin(_process)
            return result
        return _inner
    return inner
