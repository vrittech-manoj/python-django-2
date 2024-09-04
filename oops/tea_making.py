# step-1 : turn on gas 
# step-2 : put pot on gas 
# step-3 : put water on pot 
# step-4 : boil water 
# step-5 : put leaf tea pot 
# step-6: put sugar on pot 
# step-7: boil water 
# step-8 : stop gas

class TeaMaker:
    def __init__(self,sugar,tea_leaf,water):
        self.sugar = sugar
        self.tea_leaf = tea_leaf 
        self.water = water

        self.start()
    
    def start(self):
        self.gas_on()
        self.put_necessary_material()
        self.boil()
        self.gas_stop()


    def gas_on(self):
        print("congrats ! gas is on")
  

    def gas_stop(self):
        print("congrats ! gas is stop")
     

    def put_necessary_material(self):
        print(f"congrats sugar {self.sugar} gm ,tea leaf  {self.tea_leaf} gm and water {self.water} ltr is added to pot")
        # hard ware implement

    def boil(self):
        print("congrats ! water is boiled")
    

tea_maker_obj = TeaMaker(3,2,5)


