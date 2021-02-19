#.20 WAP to display the grade of student
def grade_type(x):
    y = x.upper()
    if y=="E":
        return("Excellent")
    elif y=="V":
        return("Very good")
    elif y=="G":
        return("Good")
    elif y=="A":
        return("Average")
    elif y=="F":
        return("Fail")
in_put=input("Enter grade shortcut: ")
out_put = grade_type(in_put)
print(out_put)


    
