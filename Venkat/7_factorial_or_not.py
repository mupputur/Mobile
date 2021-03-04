#7.Write a program find a factorial of a given number.
def find_factorial(inp):
    factorial=1
    for num in range(1,inp+1):
        factorial=factorial*num
    return factorial   
inp=int(input("Enter number: "))
out_put=find_factorial(inp)
print(out_put)
