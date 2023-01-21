print("Quadratic Equation Calculator")
while True:
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    if a == 0:
        x1 = -1*c/b
        x2 = "No second value of x "
    elif b == 0:
        x1 = (c**0.5)
        x2 = -1*(c**0.5)
    elif c == 0:
        x1 = (-1*b/a)**(1/2)
        x2 = -1*(-1*b/a)**(1/2)
    else:
        dis = b**2-4*a*c
        x1 = (-b+dis**(1/2))/(2*a)
        x2 = (-b-dis**(1/2))/(2*a)
    print(x1)
    print(x2)

