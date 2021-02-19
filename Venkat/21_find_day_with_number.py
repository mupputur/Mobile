#21. WAP

def find_day_with_number(inp):
    day = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
    if inp==1:
        return(day[0])
    elif inp==2:
        return(day[1])
    elif inp==3:
        return(day[2])
    elif inp==4:
        return(day[3])
    elif inp==5:
        return(day[4])
    elif inp==6:
        return(day[5])
    elif inp==7:
        return(day[6])

in_put = int(input("Enter: "))
out_put = find_day_with_number(in_put)
print(out_put)
