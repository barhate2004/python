3. Write a Python function to check whether a number is in a given range.

def isrange(n,s,e):
	if s<=n<=e:
		return 1
	else:
		return 0
n=int(input("enter a number"))
s=int(input("enter a start range"))
e=int(input("enter a end range"))
if isrange(n,s,e)==1:
	print("given number is in range")
else:
	print("given number is not in range")

