#3.WAP to check whether a given number is positive or negative..?
def check_postive_negetive(x):
    if x>0:
        return("Given number is Positive")
    elif x<0:
        return("Given number is negative")
    elif x==0:
        return("Given number is not even and not odd it's a natural number")

user_inp = float(input("Enter a number :"))
out_put = check_postive_negetive(user_inp)
print(out_put)
