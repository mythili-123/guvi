# Write a program to find all roots of a quadratic equation.


a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=float(input("enter the value of c:"))
d=(b**2)-(4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a) 
print("the solutions are",sol1,sol2)
