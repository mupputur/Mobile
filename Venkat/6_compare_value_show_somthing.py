#6.WAP to read the value of an integer m and display the value of n is 1 when m
#is lorger then 0,0 when m is 0 and -1 when m is less then 0.
def compare_show_somthing(x):
    if x>0:
        return("1")
    elif x==0:
        return("0")
    elif x<0:
        return("-1")
in_put = int(input("Enter a value: "))
out_put= compare_show_somthing(in_put)
print(out_put)
