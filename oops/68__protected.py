class Phone:
    def __init__(self) -> None:
        self.__brandname = "Apple"
        print(self.__brandname)

class Smartphone(Phone):
    def __init__(self):
        self._model_name = "Iphone 2.0"
        print("company model name ",self._model_name)
        super().__init__()

    def display(self):
        print("This is a smartphone")
        print(self._model_name)
        
smart_obj = Smartphone()
smart_obj.display()
