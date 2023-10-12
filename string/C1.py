Remove special symbols/Punctuation from a given string.
Given:
str1 = "/*Sachin is @Cricketer& kind person"
Expected Output:
“Sachin is Cricketer kind person”

s=raw_input("Enter String")
result=""
for i in s:
	if i.isalpha() or i==' ':
		result+=i

print result
