#6.Write a program find given number is perfect or not.
def perfect_or_not(inp):
    num=[]
    for i in range(1,inp):
        if inp%i==0:
            num.append(i)
    if sum(num)==inp:
        send="perfect number"
    else:
        send="not perfect number"
    return send
inp=int(input("Enter number: "))
out_put=perfect_or_not(inp)
print(out_put)
        
        
