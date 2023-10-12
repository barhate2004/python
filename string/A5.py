Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.
Sample String: 'ppk', 'abc’
Expected Result: 'abkppc’

str1=raw_input("enter string 1:\n")
str2=raw_input("enter string 2:\n")

s1=str1.replace(str1[:2],str2[:2])
s2=str2.replace(str2[:2],str1[:2])
print(s1+s2)


