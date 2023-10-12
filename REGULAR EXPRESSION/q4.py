2. Write a Python program that matches a word containing 'z'.

import re
s=input("Enter A String\t")
if(re.search(r'\b\w*z\w*\b',s)):
	print("Match Found:Given word contains z")
else:
	print("No,Entered string does not contains z")
