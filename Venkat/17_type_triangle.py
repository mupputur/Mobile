#17. WAP find type of triangle.

def type_triangle(inp1,inp2,inp3):
    if inp1+inp2+inp3 == 180:
        if inp1==inp2==inp3:
            return("Given triangle is Equilateral ")
        elif inp1!=inp2!= inp3:
            return("Given triangle is scalene")
        elif inp1==inp2 or inp2==inp3 or inp1==inp3:
            return("Given triangle is isosceles")
    else:
        return("Sum of three angles must equal to 180")
in_put = []
for i in range(3):
    in_put.append(float(input("Enter angles:")))
x,y,z=in_put
out_put = type_triangle(x,y,z)
print(out_put)
    
