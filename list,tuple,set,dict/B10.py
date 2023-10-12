Write a Python script to generate and print a dictionary that contains a number (Between 1
and n) in the form (x, x*x).
Sample Dictionary (n = 5)
Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

d={}
n=int(input("enter range"))
print("enter element of list:")
for i in range(0,n):
	k=int(input("enter key:"))
	v=k
d[k]=v*v
print("Dictionary is:")
print(d)
