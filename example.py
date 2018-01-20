from loadin.loadin import loading
import time


# example
@loading(style='point', tips='download some files')
def download():
    time.sleep(3)


@loading(style='cycle', tips='save files')
def save():
    time.sleep(3)


if __name__ == '__main__':
    download()
    save()
