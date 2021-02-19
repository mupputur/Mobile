#10.WAP to check whether a character is an alphabet,digit or special character..
def type_of_input(x):
    if x>="0" and x<="9":
        return("Given character is number :",x)
    elif (x>="A" and x<="Z") or (x>="a" and x<="z"): 
        return("Given character is alphabet:",x)    
    else:
        return("Given character is special character :",x)

in_put = input("Enter a charector :")
out_put = type_of_input(in_put)
print(out_put)
