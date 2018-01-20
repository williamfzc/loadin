import multiprocessing
import sys
from .loadin_animation import STYLE_DICT


def start_loadin(_style, _tips):
    if not (isinstance(_style, str) and isinstance(_tips, str)):
        raise TypeError('Style and tips must be str.')
    if _style not in STYLE_DICT:
        raise KeyError('Style {} not support.'.format(_style))

    ui_process = multiprocessing.Process(
        target=STYLE_DICT[_style],
        args=(_tips,)
    )
    ui_process.start()
    return ui_process


def end_loadin(_proc):
    if _proc.is_alive():
        _proc.terminate()
    sys.stdout.write('Done! \n')
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
