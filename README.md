# Loadin

> **A very very simple way to apply terminal-animation to your function!**

## Usage ##
ALL YOU NEED is a decorator:

	from loadin.loadin import loading


	@loading(style='cycle', tips='loading')
	def ha():
	    import time
	    time.sleep(3)

It's DONE!

![](demo.gif)

## Bug ##

Please contact me by issue.