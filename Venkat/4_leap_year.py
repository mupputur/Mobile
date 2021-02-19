#4.WAP to find whether a given year is a leap year or not..?
def leap_year_or_not(x):
    
    if (x%4)==0 and (x%100)!=0:
        return("Given year is leap year")
    elif (x%400) == 0:
        return("Given year is leap year")
    elif (x%100)==0:
        return("Given number is not a leap year")
    else:
        return("Given number is not a leap year")

user_inp = int(input("Enter year :"))
out_put = leap_year_or_not(user_inp)
print(out_put)
