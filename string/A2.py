Write a Python program to count the number of characters (character frequency) in a string.
Sample String: google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

s=raw_input("Enter String")
d=dict()
for i in s:
	if i in d:
		d[i]+=1

	else:
		d[i]=1
print d
