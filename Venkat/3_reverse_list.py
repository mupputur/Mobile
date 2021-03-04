#3.Write a program reverse the given input list.
def reverse_list(List):
    for num in List:
        List=List[::-1]
    return List
inp = [1,2,3,4,5]
out_put = reverse_list(inp)
print(out_put)
