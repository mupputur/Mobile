#16. WAP for position of quadrent.

def quadrent_position(inp1,inp2):
    if inp1 > 0 and inp2 >0:
        return("First quadrant")
    elif inp1 < 0 and inp2 >0:
        return("Second quadrant")
    elif inp1 > 0 and inp2 < 0:
        return("Third quadrant")
    elif inp1 < 0 and inp2 < 0:
        return("Fourth quadrant")
    elif inp1==0 or inp2==0:
        return("Coordinate value lies on vertical or horizontal line")
inp1 = float(input("Enter first coordinate :"))
inp2 = float(input("Enter second coordinate :"))
out_put = quadrent_position(inp1,inp2)
print(out_put)
