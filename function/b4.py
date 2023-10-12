4. Write a Python program to find the sum of all prime numbers till ‘n’.

n=int(input('enter number:'))
sum1=0
for j in range (2,n+1):
	f1=0
	for i in range (2,j//2+1):
			if(j%i==0):
				f1=1
				break
	if(f1==0):
		print(j)
		sum1=sum1+j
print ("sum is:",sum1)
