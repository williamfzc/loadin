from loadin.loadin import loading


# example
@loading(style='cycle', tips='loading')
def ha():
    import time
    time.sleep(3)


if __name__ == '__main__':
    ha()