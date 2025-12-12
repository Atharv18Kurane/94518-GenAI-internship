import area_cal
print("Area Calculator")

Side=float(input("enter side of square:"))
print("area of square is:", area_cal.area_square(Side))

Radius=float(input("enter radius of circle:"))
print("area of circle is:",area_cal.area_circle(Radius))

Length=float(input("enter length of rectangle:"))
Breadth=float(input("enter breadth of rectangle:"))
print("area of rectangle is:",area_cal.area_rectangle(Length,Breadth))

Base=float(input("enter base of triangle:"))
Height=float(input("enter height of triangle:"))
print("area of triangle is:",area_cal.area_triangle(Base,Height))