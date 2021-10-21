radius=float(input("Enter the Radius of the circle: "))
pi=22/7
area=pi*(radius**2)
circumference=2*pi*radius
command=input("area or circumference: ")
if command=='area':
    print(area)
elif command=='circumference':
    print(circumference)


