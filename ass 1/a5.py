 Write a program which prints Fibonacci series of a number.

n = int(input("Enter the number of teres: "))

n1 = 0
n2 = 1

count1 = 0

if n <= 0:
	print("please enter a postive number")
elif n == 1:
	print("Fibonaci sequence upto",n,":")
	print(n1)
else:
	print("Fibbonaci Sequence:")
	while count1 < n:
		print(n1)
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count1 += 1
