#18.WAP if possible or not with this angles.

def triangle_posibility(x,y,z):
    sum = x+y+z
    if sum==180:
        return("Triangle will form with this angles ")
    else:
        return("sum of given three angles are more than or less than 180,so not possible:" )
in_put = []
for i in range(3):
    in_put.append(float(input("Enter angles: ")))
x,y,z=in_put
out_put = triangle_posibility(x,y,z)
print(out_put)
    
