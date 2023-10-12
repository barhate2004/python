2. Write a Python program to remove duplicate elements from the list.

l=[]
n=int(input("enter range:"))
print("enter element of list")
for i in range(0,n):
	y=int(input())
	l.append(y)
print("list is:")
print(l)
s=set(l)
l1=list(s)
print("list without duplicate element is:")
print(l1)
