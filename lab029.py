#Triangle classifier


a=int(input('Enter side1 value'))
b=int(input('Enter side2 value'))
c=int(input('Enter side3 value'))


if a==b and b==c:
    print("Equilateral Triangle")
elif a==b and b!=c:
    print("Isosceles Triangle")
else:
    if a!=b and b!=c:
        print(("Scales Triangle"))