class Person:
    __employment = 0
    name = "Unknown"
    age = 0

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def setEmployment (self, employment):
        self.__employment = employment

    def setEmploymentView (self, size = 5):
        stars = ""
        for i in range(size):
            if i/size < self.__employment/100:
                stars += "*"
            else:
                stars += "-"
        return stars

    def setEmploymentView (self, star, size = 5):
        stars = ""
        for i in range(size):
            if i/size < self.__employment/100:
                stars += star
            else:
                stars += "-"
        return stars

    def View (self):
        print("Name: " + self.name + "\nAge: " + str(self.age) + "\nEmployment: |" + self.setEmploymentView() + "|")

class Student (Person):
    course = "Unknown"

    def setCourse (self, course):
        self.course = course

    def setEmployment (self, employment):
        Person.setEmployment(self, employment*2)

    def View (self):
        print("Name: " + self.name + "\nAge: " + str(self.age) + "\nCourse: " + str(self.course) + "\nEmployment: |" + self.setEmploymentView("#")+"|")

class Headman (Student):
    def setEmployment (self, employment):
        Person.setEmployment(self, employment*3)

person = Student("Vitaliy Danylyk", 19)
person.setCourse(3)
person.setEmployment(30)
person.View()
