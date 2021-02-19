#14. WAP for student eligibility sor professional cource.
def eligibility_profe_cource(x,y,z):
    sub_total = x+y+z
    two_sub_total = x+y
    if x>=65 and y>=55 and z>=50 and sub_total >=180:
        return("You are eligible to professional course")
    elif two_sub_total>=140:
        return("You are eligible to professional course")
    else:
        return("You are not eligible")
in_put = []
for i in range(3):
    in_put.append(int(input("enter marks:maths next physics next chemistry: ")))
m1,m2,m3 = in_put
out_put = eligibility_profe_cource(m1,m2,m3)
print(out_put)
