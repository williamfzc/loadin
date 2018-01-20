from loadin.loadin import loading


# example
@loading(style='cycle', tips='loading')
def ha():
    import time
    for i in range(3):
        time.sleep(1)


if __name__ == '__main__':
    ha()