#9) Write a Python program to convert temperatures to and from Celsius, Fahrenheit. [Formula: c/5 = f-32/9]
print("Options are\n1.Convert Temperature from Celsius to Fahrenheit\n2.Convert temperature from Fahrenheit to Celsius\n")
option=int(input("Enter your Option 1 or 2 : "))
if option==1:
    print("Convert Temperature from Celsius to Fahrenheit.")
    celsius=float(input("Enter Temperature in Celsius : "))
    fahrenheit=(celsius*9/5)+32
    print("Temperature in Fahrenheit is : ",fahrenheit)
elif option==2:
    print("Convert Temperature from Fahrenheit to Celsius.")
    fahrenheit=float(input("Enter Temperature in Fahrenheit : "))
    Celsius=(fahrenheit-32)*5/9
    print("Temperature in Celsius is : ",Celsius)
else:
    print("Entered option is Invalid Option")
