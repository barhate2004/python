Create a function showEmployee() in such a way that it should accept employee name,
and it’s salary and display both, and if the salary is missing in function call it should
show it as 9000

def showEmployee(ename,esalary):
	print("Employee name",ename)
	print("Employee salary",esalary)
ename=raw_input("Employee Name:")
esalary=raw_input("Employee Salary:")
if(esalary==""):
	showEmployee(ename,esalay=9000)
else:
	showEmployee(ename,esalary)
