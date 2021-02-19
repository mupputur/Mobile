#24.
def shape_area(inp):
    if inp =="circle":
        radies = float(input("Enter circle radies:"))
        return("Circle area :",(1/2*(3.14*radies*radies)))

    elif inp =="rectangle":
        length = float(input("Enter length :"))
        width = float(input("Enter width :"))
        return("Area of rectangle :",(length*width))
        
    elif inp =="triangle":
        height = float(input("Enter height :"))
        base = float(input("Enter base :"))
        return("Area of triangle :",(1/2*(base*height)))
in_put = input("Enter shape type :")
out_put = shape_area(in_put)
print(out_put)
