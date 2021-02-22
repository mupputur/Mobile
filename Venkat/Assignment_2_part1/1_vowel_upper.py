#1.Write a program convert all the vowels to uppercase for
#the given input string.
def vowel_upper(string):
    vowel=("a","e","i","o","u")
    out_put = ""
    for ch in string:
        if ch in vowel:
            value=ord(ch)-32
            send=chr(value)
            out_put = out_put+send
        else:
            out_put=out_put+ch
    return out_put
inp1 = input("Enter input: ")
out_put =vowel_upper(inp1)
print(out_put)
        
    
