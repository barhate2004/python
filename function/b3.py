3. Write a Python program to filter a list of integers using Lambda


numbers=[1,2,3,4,5,6,7,8,9,10]

filtered_numbers=list(filter(lambda x:x%2==0,numbers))

print("Filtered numbers (even): ",filtered_numbers)
