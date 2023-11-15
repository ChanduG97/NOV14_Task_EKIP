#8) Write a python program to find largest of three numbers.

num1=int(input("Enter Number 1 : "))
num2=int(input("Enter Number 2 : "))
num3=int(input("Enter Number 3 : "))
print('-'*70)
if(num1>num2)and(num1>num3):
    print("NUM 1 = ",num1," is Largest")
elif(num2>num1)and(num2>num3):
    print("NUM 2 = ",num2," is Largest")
elif(num3>num1)and(num3>num2):
    print("NUM 3 = ",num3," is Largest")
else:
    print("All numbers are Equal")
print('-'*70)