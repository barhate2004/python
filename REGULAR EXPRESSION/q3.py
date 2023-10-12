1. Write a Python program that matches a word at the beginning of a string.

import re
s=raw_input("Enter a string\t")
a=raw_input("Enter a word to be search it matches at starting\t")
if(re.search(r'^'+re.escape(a),(s))):
	print("Yes,The String starts with given word",a)
else:
	print("No,The String does not start with given word")
