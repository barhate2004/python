2. Write a NumPy program to get the unique elements of an array.

import numpy as np
l=[]
n=int(input('enter how many numbers'))
for i in range(1,n+1):
	x=int(input('enter number'))
	l.append(x)
a=np.array(l)
print (a)
b=[]
for i in a:
	if i not in b:
		b.append(i)
a1=np.array(b)
print (a1)
