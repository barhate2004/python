Write a program which finds sum of digits of a number.
Example n=130 then output is 4 (1+3+0)
a=int(input("Enter Number"))
sum=0
r=0
while a>0:
	r=a%10
	sum=sum+r
	a=a/10
print("sum of digit",sum)
