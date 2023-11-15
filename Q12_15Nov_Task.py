#12) Write a python program to find factorial of a number using Recursion.
def Rec_fact(n):
    if n==1:
        return n
    else:
        return n*Rec_fact(n-1)
num=int(input("Enter a number: "))
if num<0:
    print("Entered Number is negative number.")
elif num==0:
    print("The Factorial of 0 is 1")
else:
    print("The factorial of ",num,"is ",Rec_fact(num))