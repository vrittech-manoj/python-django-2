class Employee:
    def __init__(self,name,current_salary): #5000 , bonus, tax
        self.name = name 
        self.current_salary = current_salary 
        print(f"{self.name} current salary is {self.current_salary}")
        self.bonus()
        self.tax()
      
    def bonus(self):
        #bonus with price
        bonus = 200
        self.bonus_s = bonus 
        print(f"bonus is added to {self.name}",self.bonus_s)

    def tax(self):
        #tax with price
        tax = 0.2
        self.tax_with_salary = tax/100*self.current_salary
        print(f"tax is deducted from {self.name}",self.tax_with_salary)
    
    def total_salary(self):
        #total salary with price
        self.total_salary = self.current_salary + self.bonus_s - self.tax_with_salary
        print("total salary ",self.total_salary,"\n**********************")




staff_data = [{"name":"umesh","salary":40000},{"name":"pradeep","salary":60200},{"name":"sagar","salary":19500}]

for data in staff_data:
    user_name = data['name']
    user_salary = data['salary']

    
    obj = Employee(user_name,user_salary)
    obj.total_salary()
    data['bonus'] = obj.bonus_s
    data['tax'] = obj.tax_with_salary
    data['total_salary'] = obj.total_salary




print("\n\n\n")
print(staff_data)



#iron dome 



