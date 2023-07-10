def myFun(arg1, **argv):
	print("First argument :", arg1)
	for arg in argv:
		
		print("Next argument through *argv :", argv["a"])


myFun("ff",a='Hello', b= 'Welcome', c='to', d ='GeeksforGeeks')
