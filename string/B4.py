4. Write a Python program to count the occurrences of each word in a given sentence.

s=raw_input("Enter String :")
l=s.split(' ')
print (l)
for i in l:
	c=l.count(i)
	print("occurence of %s"%i)
	print("%d"%c)
