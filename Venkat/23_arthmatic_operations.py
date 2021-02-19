#23. WAP
def arthmatic_operations(x,y,z):
    if inp3=="+":
        return(inp1+inp2)
    elif inp3=="-":
        return(inp1-inp2)
    elif inp3=="*":
        return(inp1*inp2)
    elif inp3=="%":
        return(inp1%inp2)
    elif inp3=="/":
        return(inp1/inp2)
    elif inp3=="//":
        return(inp1//inp2)
inp1 = int(input("Enter 1st numbe:"))
inp2 = int(input("Enter 2nd numbe:"))
inp3 = input("Enter oparater:")
out_put = arthmatic_operations(inp1,inp2,inp3)
print(out_put)

    
