print("*****Area Calculator*****")
print("Press 1 for finding area of Square \n Press 2 for finding area of Rectangle" \
"\n Press 3 for finding area of Circle \n Press 1 for finding area of Triangle \n")
entry=int(input("Enter the choice "))
if entry==1:
    side=float(input("Enter the side of square"))
    area=side**2
    print("Area of the square is ",area)
elif entry==2:
    length=float(input("Enter the length of rectangle "))
    breadth=float(input("Enter the breadth of rectangle "))
    area=length*breadth
    print("Area of the rectangle is ",area)
elif entry==3:
    radius=float(input("Enter the radius of circle "))
    area=3.14*radius*radius
    print("Area of the circle is ",area)
elif entry==4:
    base=float(input("Enter the base length "))
    height=float(input("Enter the height length "))
    area=0.5*base*height
    print("Area of the triangle is ",area)
else:
    print("Wrong input")