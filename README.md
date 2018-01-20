# Loadin

> **A very very simple way to apply terminal-animation to your function!**

## Setup ##

    pip install loadin

## Usage ##
ALL YOU NEED is a decorator:

	from loadin.loadin import loading


    @loading(style='point', tips='download some files')
    def download():
        time.sleep(3)


    @loading(style='cycle', tips='save files')
    def save():
        time.sleep(3)


    if __name__ == '__main__':
        download()
        save()


It's DONE!

![](demo.gif)

## Bug ##

Please contact me by issue.