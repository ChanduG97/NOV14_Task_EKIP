#13) Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides).  


base=float(input("enter the length of Base :"))
perp=float(input("enter the length of perpendicular :"))
hypo=float(input("enter the length of Hypotenuse :"))

if hypo**2==((base**2)+(perp**2)):
    print("it is right angle triangle")
else:
    print("it is not a right angle triangle")