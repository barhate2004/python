2. Write a Python program to find the position of minimum and maximum elements of a list

l=[]
n=int(input("enter range:"))
print("enter element of list:")
for i in range(0,n):
	y=int(input())
	l.append(y)
print("list is:")
print(l)
lmax=l.index(max(l))
lmin=l.index(min(l))
print("position of max value",lmax)
print("position of min value",lmin)
