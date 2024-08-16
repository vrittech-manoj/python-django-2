first_list =[5, 1, 1, 9, 23, 54,-234,345345]

j=0
while j<len(first_list):
    for i in range(0,len(first_list)-1):
        if first_list[i] > first_list[i+1]:
            first_list[i],first_list[i+1] = first_list[i+1],first_list[i]
    j=j+1

print(first_list)



