# 7) Write a program to demonstrate working with dictionaries in python.
Employee_Data={'name':'Chandu','role':'Associate Engineer','ID':545}
print('-'*60)
print("Employee data is : ",Employee_Data)
print('-'*60)
print("Employee name is : ",Employee_Data['name'])
print("Employee ID is : ",Employee_Data['ID'])
print('-'*60)
print("All keys in Dictonary Employee_Data ")
for k in Employee_Data:
    print(k)
print('-'*60)
print("All values in Dictonary Employee_Data ")
for v in Employee_Data:
    print(Employee_Data[v])
print('-'*60)
print('Adding Items')
Employee_Data['phone']='9010148616'
print("Updated Dictonary is : ",Employee_Data)
print('-'*60)
print("Using POP function ",Employee_Data.pop('role'))
print("Length of Dictonary : ",len(Employee_Data))
dict1 = Employee_Data.copy()
print("Copied Dictonary is : ",dict1)
dict1.clear()
print("Updated Copy dictonary is :",dict1)
print('-'*60)
