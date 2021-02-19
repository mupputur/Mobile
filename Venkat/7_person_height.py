#7.WAP for person height
def person_height(x):
    if x < "150":
        return("DWARF")
    elif "150" <= x<= "165":
        return("AVERAGE HEIGHT")
    elif x > "165":
        return("TALL")
take_inp = input("Enter height: ")
out_put = person_height(take_inp)
print(out_put)

