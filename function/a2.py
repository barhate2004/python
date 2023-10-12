Write a Python function to multiply all the numbers in a list.
Sample-List :(8,2,3,-1,7)
Expected Output : -336

l=[]
n=int(input("enter how many numbers"))
for i in range(1,n+1):
	x=int(input('enter number'))
	l.append(x)
print l
ans=1
for i in l:
	ans=ans*i
print ans
