import multiprocessing
from functools import wraps
from sys import stdout as out
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


def end_loadin(_proc, _end_flag):
    if _proc.is_alive():
        _proc.terminate()
    if _end_flag:
        out.write('\nDone!\n')
    else:
        out.write('\n')
    out.flush()


def loading(style=None, tips=None, end_flag=None):
    tips += ' '
    if not style:
        style = 'point'
    if not tips:
        raise ValueError('tips can\'t be empty')

    def inner(func):
        @wraps(func)
        def _inner(*args, **kwargs):
            _process = start_loadin(style, tips)
            result = func(*args, **kwargs)
            end_loadin(_process, end_flag)
            return result
        return _inner
    return inner
