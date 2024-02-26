def solve(a, b, c):
    if a==0:
        x = -c/b
        print("The single value for x is:", x)
    elif b==0:
        if c>0:
            x = (c/a)**(0.5)
            print("The values of x are: ±", x, "*i")
        else:
            x = (-c/a)**(0.5)
            print("The values of x are: ±", x)
    elif c==0:
        x = -b/a
        print("The values for x are:", x, "and 0")
    else:
        dis = b**2-4*a*c
        if dis>0:
            x1 = (-b+dis**(0.5))/(2*a)
            x2 = (-b-dis**(0.5))/(2*a)
            print("The values of x are:", x1, "and ", x2)
        elif dis==0:
            x = -b/(2*a)
            print("The single value for x is:", x)
        elif dis<0:
            idis = (dis*-1)**(0.5)/(2*a)
            x = (-b)/(2*a)
            print("The values of x are:", x, "±", idis, "*i")
        else:
            print("follow the instructions please")
print("Please structure your input accordingly:")
print("(a)x^2 + (b)x + (c) = 0")
while True:
    a= int(input("a = "))
    b= int(input("b = "))
    c= int(input("c = "))
    solve(a,b,c)
