#2.Write a program reverse a given input string
def str_reverse(string):
    out_put = ""
    c = -1
    for ch in string:
        out_put=out_put+string[c]
        c= c-1
    return out_put
inp=input("Enter input: ")
out_put = str_reverse(inp)
print(out_put)
        
