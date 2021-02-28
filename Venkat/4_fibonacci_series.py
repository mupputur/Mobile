#4.Write a program print the Fibonacci series  till 100.
def fibonacci_series(inp):
    c1=0
    c2=1
    output=[c1,c2]
    for i in range(inp):
        nxt=c1+c2
        output.append(nxt)
        c1=c2
        c2=nxt
        if nxt>inp:
            break
    return output[:-1]
inp = int(input("Enter series till: "))
out_put = fibonacci_series(inp)
print(out_put)
