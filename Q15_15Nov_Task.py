#15) Write a python program to define a module and import a specific function in that module to another program.

from Q15_15Nov_Task_Arithmatic_Operations import *
num1=float(input("Enter A value : "))
num2=float(input("Enter B value : "))
print("Multiplication of ",num1," & ",num2," is ",multiply(num1,num2))
print("Addition of ",num1," & ",num2," is ",add(num1,num2))
print("Subtraction of ",num1," & ",num2," is ",sub(num1,num2))