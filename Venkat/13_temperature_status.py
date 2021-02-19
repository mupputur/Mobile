#13. WAP for temperature.
def temp_status(inp):
    if inp<0:
        return("Freezing weather")
    elif 0<=inp<10:
        return("Very cold weather")
    elif 10<=inp<20:
        return("Cold weather")
    elif 20<=inp<30:
        return("Temperature is in normal")
    elif 30<=inp<40:
        return("Its hot")
    elif inp>=40:
        return("Its very hot")
in_put = float(input("Enter temparature in celsius:"))
out_put = temp_status(in_put)
print(out_put)
