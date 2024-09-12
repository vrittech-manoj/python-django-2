from abc import ABC,abstractmethod

# class Polygon(ABC):

#     @abstractmethod
#     def noofsides(self):
#         print("this is not made in proper way.")

#     def area(self):
#         print("this is area of triangle ")


# class Triangle(Polygon):
    
#     def noofsides(self):
#         print("i have 3 sides")


# triangle_obj = Triangle()
# triangle_obj.area()
# triangle_obj.noofsides()


class Shape(ABC):

    def area_of_triangle(self,b,h):
        return 0.5*b*h 
    
    def area_of_rectangle(self,l,b):
        return l*b 
    
    @abstractmethod
    def area_of_square(self,l):
        print("i don't now , please  you must do it.")
