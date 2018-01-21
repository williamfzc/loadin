import multiprocessing
from functools import wraps
from sys import stdout as out
from .loadin_animation import STYLE_DICT
from .conf import MAX_LENGTH, CYCLE_TIME, SPEED_DICT


def clean_board(_length):
    out.flush()
    out.write('\x08'*_length + ' '*_length + '\x08'*_length)
    out.flush()


def start_loadin(_style, _tips, _speed):
    if not (isinstance(_style, str) and isinstance(_tips, str)):
        raise TypeError('Style and tips must be str.')
    if _style not in STYLE_DICT:
        raise KeyError('Style {} not support.'.format(_style))

    ui_process = multiprocessing.Process(
        target=STYLE_DICT[_style],
        args=(_tips, _speed)
    )
    ui_process.start()
    return ui_process


def end_loadin(_proc, _end_flag):
    if _proc.is_alive():
        _proc.terminate()
    # clean the board
    clean_board(MAX_LENGTH)
    # check end flag
    if _end_flag:
        out.write('Done!\n')
    out.flush()


def loading(tips, style=None, end_flag=False, speed=CYCLE_TIME):
    # args check
    if not style:
        style = 'point'
    if not tips:
        raise ValueError('tips can\'t be empty')
    if not isinstance(end_flag, bool):
        raise TypeError('end_flag must be True or False')
    if speed != CYCLE_TIME:
        if speed not in SPEED_DICT:
            raise KeyError('Speed must be selected in fast/normal/slow.')
        else:
            speed = SPEED_DICT[speed]

    tips += ' '

    def inner(func):
        @wraps(func)
        def _inner(*args, **kwargs):
            _process = start_loadin(style, tips, speed)
            result = func(*args, **kwargs)
            end_loadin(_process, end_flag)
            return result
        return _inner
    return inner
