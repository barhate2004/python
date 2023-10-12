 Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’.

n = int(input("Enter the end limit"))
n+=1

for val in range(1,n):
	if val>1:
		for i in range(2,val):
			if(val % i)==0:
				break;
		else:
			print(val)
