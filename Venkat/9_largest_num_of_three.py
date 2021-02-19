#9.WAP to find the largest number of three numbers..?
def larg_num_of_three(x,y,z):
    if y<x>z and x!=y and x!=z or y==z:
        return("Maximum nimber is:",x)
    elif y<x>z and y==z:
        return("Maximum nimber is:",x)
    elif x<y>z and y!=x and y!=z or z==x:
        return("Maximum nimber is:",y)
    elif x<y>z and z==x:
        return("Maximum nimber is:",y)
    elif x<z>y and z!=x and z!=y or y==x:
        return("Maximum nimber is:",z)
    elif x<z>y and y==x:
        return("Maximum nimber is:",z)
    elif x==y==z:
        return("you entered three numbers same")

#in_put1 = input("Enter the 1st Number: ")
#in_put2 = input("Enter the 2nd Number: ")
#in_put3 = input("Enter the 3rd Number: ")
in_put =[]
for num in range(3):
    in_put.append(input("Enter value: "))
a,b,c = in_put
#print(x,y,z)
out_put = larg_num_of_three(a,b,c)
print(out_put)
