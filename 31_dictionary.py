my_data = {"name":"skill shikshya","location":"kathmandu","district":"bagmati"}
keys = my_data.keys() #this return all keys 
values = my_data.values() #this return all  values

second_data = my_data.copy()
my_data.pop("district")



print(second_data)

