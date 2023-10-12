Write a Python program to remove a key from a dictionary.
Sample Dictionary: myDict={'a':1,'b':2,'c':3,'d':4}
Sample Output: {'c': 3, 'b': 2, 'd': 4, 'a': 1}
{'c': 3, 'b': 2, 'd': 4}

d={}
n=int(input("enter range"))
print("enter element of list:")
for i in range(0,n):
	k=input("enter key:")
	v=int(input("enter values:"))
d[k]=v
print("dictonary is:")
print(d)
print(k)
print("directory deleted key is:")
print(d)
