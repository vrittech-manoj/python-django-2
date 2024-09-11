

class Smartphone():
    def __init__(self):
        self.__model_name = "Iphone 2.0"
        print("company model name ",self.__model_name)

    def display(self):
        print("This is a smartphone")
        print(self.__model_name)
        
smart_obj = Smartphone()
# smart_obj.display()
print("modify model name ",smart_obj.__model_name)  # Output: Iphone m2


# public
# private
# protected