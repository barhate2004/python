Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the empty string.
Sample String : 'General12'
Expected Result : 'Ge12'
Sample String : 'Ka'
Expected Result : 'KaKa'
Sample String : ' K'
Expected Result : Empty String

s=raw_input("Enter String")
if len(s)<2:
	print "Empty String"
elif(len(s))==2:
	print s+s
else:
	print s[:2]+s[len(s)-2:len(s)]
