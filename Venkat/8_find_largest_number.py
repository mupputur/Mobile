#8. WAP find lorgest of two numbers..?
def largest_num_of_two(a,b):
    if a>b:
        return("This is the largest Number: ",a)
    elif a<b:
        return("This is the largest Number: ",b)
    else:
        return("Both are Equal Numbers")
take_inp1 = input("Enter first Number: ")
take_inp2 = input("Enter second Number: ")
out_put = find_largest_number(take_inp1,take_inp2)
print(out_put)
