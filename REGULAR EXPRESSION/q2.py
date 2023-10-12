Write a Python program to find the sequences of one upper case letter followed by lower case
letters.

import re
s=raw_input("Enter a string\t")
if(re.search(r'[A-Z][a-z]+',s)):
	print("Yes,the entered string starts with uppercase followed by lowercase")
else:
	print("No,the entered string does not start with the upper case followed by lowercase")
