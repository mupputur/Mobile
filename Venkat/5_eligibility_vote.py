#5.WAP to read the age of a candidate and determind whether it is
#eligible for casting his/her own vote..?
def eligible_vote(age):
    if age>"18":
        return("You are eligible for casting vote")
    else:
        return("You are eligible for casting vote")
inp_age = input("Enter age of the person: ")
out_put = eligible_vote(inp_age)
print(out_put)
