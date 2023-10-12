Write a NumPy program to test whether each element of a 1-D array is also present in a second
array.
import numpy as np
l=[]
n=int(input('enter how many numbers'))
for i in range(1,n+1):
	x=int(input('enter number'))
	l.append(x)
a=np.array(l)
print (a)
l1=[]
n=int(input('enter how many numberss'))
for i im range(1,n+1):
	x==int(input('enter numbers'))
	l1.append(x)
b=np.array(l1)
print (b)
f1=0
for i in a:
	if i in b:
		print(i,"present in array")
	f1=1
if(f1==0):
	print("all are unique")
