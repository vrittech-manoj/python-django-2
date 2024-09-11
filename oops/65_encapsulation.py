class Smartphone():
    def __init__(self):
        self.model_name = "Iphone 2.0"
        print("company model name ",self.model_name)
smart_obj = Smartphone()


smart_obj.model_name = "Iphone 5.0"
print("modify model name ",smart_obj.model_name)  # Output: Iphone m2


# public
# private
# protected