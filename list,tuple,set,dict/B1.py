1. Write a Python program to print list after removing ODD numbers.

l=[]
n=int(input('enter how many numbers'))
for i in range(1,n+1):
	x=int(input('enter number'))
	l.append(x)
l1=[]
for i in l:
	if i%2==0:
		l1.append(i)
print l1
