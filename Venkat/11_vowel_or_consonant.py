#11.WAPto check whether an alphabet is a vowel or consonant..?

def vowel_or_consonant(x):
    vowel = ("A","E","I","O","U")
    conv_upper = x.upper()
    if conv_upper in vowel:
        return("Given alphabet is vowel:",x)
    else:
        return("Given alphabet is consonant:",x)
in_put = input("Enter an alphabet :")
out_put = vowel_or_consonant(in_put)
print(out_put)
