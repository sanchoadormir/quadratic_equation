a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if b == 0:
    x1 = (c**0.5)
    x2 = -1*(c**0.5)
elif c == 0:
    x1 = 0
    x2 = -1*b/a
else:
    x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
print(x1)
print(x2)
