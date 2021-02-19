#15. WAP for student result class.
def student_result_class(name,num):
    y = 0
    for i in range(0,3):
        marks = int(input("Enter subject maximu marks(100) and click on enter button :"))
        y=y+marks
    if (y/300)*100 >=60:
        return("First")
    elif 60>(y/300)*100 >=48:
        return("Second")
    elif 48>(y/300)*100 >=36:
        return("Pass")
    elif 36>(y/300)*100:
        return("Fail")

name = input("Enter student name :")
num = input("Enter roll number :")
out_put = student_result_class(name,num)
print(out_put)
