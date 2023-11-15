#11) Write a Python script that prints prime numbers less than 20.
print("Prime Numbers between 1 & 20 are : ")
end=20
for i in range(end):
    if i >1:
        for k in range(2,i):
            if(i%k)==0:
                break
        else:
            print("Prime Number ",i)