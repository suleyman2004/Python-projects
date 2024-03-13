x=float(input("Enter x:"))
y=float(input("Enter y:"))
triangle_area=1/2*x*(y-0.8*y)
rectangle_area=0.8*y*x/2
total_area=triangle_area+rectangle_area
print("Total area of the shape is %.2f square units" %total_area)
