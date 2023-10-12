2. Write a recursive function to calculate the sum of numbers from 0 to 10.

def sum_range(num):
	if(num==0):
		return 0;
	return(num+sum_range(num-1))
n=int(input("Enter number :"))
x=sum_range(n)
print("Sum=",x)
