class University:
    def __init__(self):
        self.university_name = "Tribhuvan University"

    def display_staff(self):
        print("**************displaying staff******************")
        for staff in self.teachers:
            print(staff)

class Country:
    def __init__(self):
        self.country_name = "nepal"


class College(University,Country):
    def __init__(self, college_name):
        self.college_name = college_name 
        self.teachers = []

        University.__init__(self)
        Country.__init__(self)


    def add_teachers(self,name,department):
        teacher_name = name 
        department = department
        self.teachers.append({"teacher_name":teacher_name,"department":department,"college":self.college_name,"university":self.university_name})
        print("teacher is added ")  

    def display_teachers(self):
        print(self.teachers)

college_obj = College("NCC")
college_obj.add_teachers("manoj","IT department")
college_obj.add_teachers("janak","Math")
college_obj.add_teachers("dinesh","science")
college_obj.display_staff()



