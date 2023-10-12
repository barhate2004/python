Write a Python program to perform different set operations.
Expected Output:
{'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
15
25
35
x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]

s1=set()
s2=set()
n1=int(input("enter range"))
print("enter element of set")
for i in range(0,n1):
	y=int(input())
	s1.add(y)
print("element of set 1 is:")
print(s1)
n2=int(input("enter range"))
print("enter element of set")
for i in range(0,n2):
	z=int(input())
	s2.add(z)
print("element of set 1 is:")
print(s2)
print("union of set 1 and set 2 is:")
print(s1|s2)
print("intersection of set 1 and set 2 is:")
print(s1&s2)
print("difference of set 1 and set 2 is:")
print(s1-s2)
print("symmetric of set 1 and set 2 is:")
print(s1^s2)
