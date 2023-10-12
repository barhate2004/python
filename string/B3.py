3. Write a Python program to remove the characters which have odd index values of a given string.

s=raw_input("Enter String")
r=""
for i in s:
	n=s.index(i)
	if n%2==0:
		r+=i

print r
