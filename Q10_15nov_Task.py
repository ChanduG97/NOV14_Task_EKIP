# 10) Write a Python program to construct the stars(*) pattern, using a nested for loop
n=int(input("Enter a Range : "))
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print('')