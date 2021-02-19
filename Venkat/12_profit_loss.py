#12. WAP for profit or loss

def profit_loss(x,y):
    diff = x-y
    if diff<0:
        return( "profit :",(y-x))
    elif diff>0:
        return("loss :",(x-y))
    elif x==y:
        return("No profit no loss")
cp = float(input("Enter cost price :"))
sp = float(input("Enter selling price :"))
out_put = profit_loss(cp,sp)
print(out_put)
