Write a Python program to match a string that contains only upper and lowercase letters,
numbers, and underscores.
import re
s=raw_input("Enter a string\t")
if(re.search(r'^[A-Za-z0-9_]+$',s)):
	print("String contains given number of characters")
else:
	print("String does not contains a-z , A-Z and 0-9,underscores")
