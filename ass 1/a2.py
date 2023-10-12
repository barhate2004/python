/*Write a program which accepts 6 integer values and prints “DUPLICATES” if any of the
values entered are duplicates otherwise it prints “ALL UNIQUE”.
Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed//
l=list();
n=int(input("enter how many numbers you want to list"))
for i in range(1,n+1):
	l.append(input("enter data"))
for i in range(0,n+1):
	for j in range(i+1,n):
		if(l[i]==l[j]):
			print "duplicates present"
			exit()
print "all unique"
