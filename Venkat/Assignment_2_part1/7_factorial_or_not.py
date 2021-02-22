#7.Write a program find a factorial of a given number.
def find_factorial(inp):
    out=1
    for i in range(1,inp+1):
        out=out*i
    return out   
inp=int(input("Enter number: "))
out_put=find_factorial(inp)
print(out_put)
