from loadin.loadin import loading
import time


# example
@loading(style='point', tips='download some files', end_flag=True)
def download():
    time.sleep(3)


@loading(style='cycle', tips='save files')
def save():
    for i in range(3):
        time.sleep(1)


if __name__ == '__main__':
    download()
    save()
