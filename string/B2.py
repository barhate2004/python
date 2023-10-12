2. Write a Python program to calculate the Number of Digits and Letters in a string.

s=raw_input("Enter String")
d=0
l=0
for i in s:
	if i.isdigit():
		d+=1
	if i.isalpha():
		l+=1

print "number of digits:",d
print "number of letters:",l
