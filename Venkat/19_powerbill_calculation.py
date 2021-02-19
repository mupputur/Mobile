#19.WAP
def powerbill_calculation(inp1,inp2,inp3):
    inp3 = float(inp3)
    if inp3<=199:
        return(inp1,inp2,float(inp3*1.20))
    elif 200<=inp3<400:
        return(inp1,inp2,float(inp3*1.50))
    elif 400<=inp3<600:
        return(inp1,inp2,float(inp3*1.80))
    elif 600<=inp3:
        return(inp1,inp2,float(inp3*2.0))
in_put = []
for i in range(3):
    in_put.append(input("Enter customer:id,name,units : "))
x,y,z=in_put
out_put = powerbill_calculation(x,y,z)
print(out_put)
    
