#4.Write a program print the Fibonacci series  till 100.
def fibonacci_series(inp):
    total=[]
    c=0
    for i in range(2):
        total.append(c)
        c=c+1
    else:
        if len(total)<=2 :
            for num in range(inp):
                series= total[num]+total[num+1]
                total.append(series)
                if total[-1]>inp:
                    break
    total.pop()
    return total
inp = int(input("Enter series till: "))
out_put = fibonacci_series(inp)
print(out_put)
