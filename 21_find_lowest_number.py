#WAP to find lowest number amongs  "822457313496"

data = "822457313496"

lowest_number = 999999

for number in data:
    number = int(number)

    if number < lowest_number:
        lowest_number = number 
    
print("lowest number is :",lowest_number)


