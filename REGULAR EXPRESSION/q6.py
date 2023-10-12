Write a Python program to search for a literal string in a string and also find the location
within the original string where the pattern occurs.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'

import re
text=raw_input("Enter a string\t")
pattern=raw_input("Enter a word to be search\t"
print('"Searching for "%s" in "%s"'%(Pattern,text))
if(re.search(Pattern,text)):
	print("Yes entered pattern found at position:")
	print(text.find(pattern))
else:
	print("Match not found")
