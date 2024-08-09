#WAP to take user input email and validate wether it is correct email or not
#WAP to take user input mark percentage and find their division.


mark_percentage = input("Enter your mark percentage#>>>. ")
mark_percentage = int(mark_percentage)
if mark_percentage<30:
    print("fail")
elif mark_percentage>30 and mark_percentage<40:
    print("third division")
elif mark_percentage>40 and mark_percentage<60:
    print("second division")
elif mark_percentage>60 and mark_percentage<80:
    print("first divi.")
else:
    print("distinction")





