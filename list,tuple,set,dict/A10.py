Write a Python program to sum all the items in a dictionary.
Sample Dictionary: my_dict={'data1':100,'data2':-54,'data3':247}
Expected Result: 293
d={}
n=int(input("enter range"))
print("enter element of list:")
for i in range(0,n):
	k=input("enter key:")
	v=int(input("enter values:"))
d[k]=v
print(d)
sum1=sum(d.values())
print("sum of value is:")
print(sum1)
