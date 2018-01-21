from loadin.loadin import loading
# if you install loadin by pip, here may be:
# from loadin import loading
import time


# example
@loading(style='wave', tips='download some files', end_flag=True)
def download():
    time.sleep(3)


@loading('download')
def save():
    for i in range(3):
        time.sleep(1)


if __name__ == '__main__':
    download()
    save()
