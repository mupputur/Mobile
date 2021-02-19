#22.WAP
def find_days_in_month(inp):
    month = ("JAN 31 days","Feb 28 days ","MAR 31 days","APR 30 days","MAY 31 days ",
    "JUN 30 days","JUL 31 days","AUG 31 days","SEP 30 days","OCT 31 days","NOV 30 days","DEC 31 days")
    if inp>=0 and inp<=12:
        return(month[inp-1])

in_put = int(input("Enter number of month :"))
out_put = find_days_in_month(in_put)
print(out_put)
