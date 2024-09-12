
from shape import Shape

class Myshape(Shape):

    def area_of_circle(self,r):
        return 3.14*r*r
    
    def area_of_square(self, l):#this i abstract method so i should must implement
        return l*l



shape_obj = Myshape()
print("area of triangle is ",shape_obj.area_of_triangle(20,10))
print("area of rectangle is ",shape_obj.area_of_rectangle(l=30,b=40))
print("area of circle is ",shape_obj.area_of_circle(r=10))
print("area of square is ",shape_obj.area_of_square(5))

