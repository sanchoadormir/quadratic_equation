a = input("a = ")
b = input("b = ")
c = input("c = ")

if not a.isnumeric() or not b.isnumeric() or not c.isnumeric():
    print("Input values must be numbers")
else:
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a == 0:
        print("The coefficient of x^2 cannot be zero")
    else:
        dis = b**2 - 4*a*c
        if dis < 0:
            print("The solutions are complex numbers")
        else:
            x1 = (-b + (dis)**(1/2))/(2*a)
            x2 = (-b - (dis)**(1/2))/(2*a)
            print("x1 = ", x1)
            print("x2 = ", x2)
