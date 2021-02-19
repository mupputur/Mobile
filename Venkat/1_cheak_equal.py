#1.WAP to accept two integers and check whether they are equal or not..?

def check_equal(x,y):
    if x==y:
        return("Given two numbers are Equal")
    else:
        return("Given two numbers are not Equal")
first_num = int(input("Enter first Number: "))
second_num = int(input("Enter second Number: "))
out_put = check_equal(first_num,second_num)
print(out_put)
