# only one signature but many form 
# overloading

# def add(a,b,c=0):
#     print(a+b+c)


# add(4,7)
# add(4,7,8)

#overiding
class Animal:
    def sound(self):
        print("this is animal sound")

class Cat(Animal):
    
    def sound(self):
        print("meu meu ....")

cat_obj = Cat()
cat_obj.sound()


class Mathematics:
    def add(self,a,b):
        print(a+b)

    def sub(self,a,b):
        print(a-b)
    
    def mul(self,a,b,c=1):
        print(a*b*c)





#







