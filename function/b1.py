Write a Python function that takes a number as a parameter and check the number is
prime or not.

def chk_prime(n):
	flag=1
	for i in range(2,n):
		if(n%i==0):
			flag=0
			print("Not Prime")
			break;
	if(flag==1):
		print("PRIME")
n=int(input("Enter Number :"))
chk_prime(n)
