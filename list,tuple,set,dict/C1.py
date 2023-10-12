Write a Python program to create a dictionary from a string.
Sample-String:’W-resource’
Expected output: {'-': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

s=raw_input("enter string:")
s1={}
for i in s:
 if i in s1:
  s1[i]+=1
 else:
  s1[i]=1
print("frequency of every char is:"+str(s1));
