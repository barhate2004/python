Write a program which accepts an integer value as command line and print “Ok” if value is
between 1 to 50 (both inclusive) otherwise it prints” Out of range”

n=int(input("Enter number"))

if(n>0 and n<50):
	print"ok"
else:
	print"out of range"
