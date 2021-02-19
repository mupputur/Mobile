#2.WAP to check whether a given number is even or odd..?
def even_odd(x):
    if x%2==0 or x==0:
        return("Given Number is Even")
    else:
        return("Given Number is Odd")
in_put = int(input("enter number:"))
out_put = even_odd(in_put)
print(out_put)
