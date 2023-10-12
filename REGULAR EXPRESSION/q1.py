Write a Python program to check that a string contains only a certain set of characters (in this
case a-z, A-Z and 0-9).

import re
s=raw_input("Enter a string\n");
if(re.match(r'\w',s)):
	print("String contains given set of characters")
else:
	print("String does not contains a-z , A-Z and 0-9")

