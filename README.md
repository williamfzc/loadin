# Loadin
[![PyPI](https://img.shields.io/pypi/v/loadin.svg)](https://pypi.python.org/pypi/loadin)
[![codebeat badge](https://codebeat.co/badges/3cc04ca8-2dec-4281-8abd-c4281f9df5de)](https://codebeat.co/projects/github-com-williamfzc-loadin-master)

> **A very very simple way to apply terminal-animation to your function!**

## Setup ##

    pip install loadin

## Usage ##
ALL YOU NEED is ONE-LINE:

    @loading(tips='download some files')
    def download():
        time.sleep(3)


    if __name__ == '__main__':
        download()

OR more animation:

	from loadin import loading


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

## Args ##

- **tips**: any string, can't be empty
- **style**: 'point', 'cycle'
- **end_flag**: True or False


## Bug ##

Pull requests, issues, comments and suggestions welcome.