#SRP

class Person:
    def __init__(self, name: str):
        self.name = name

    def Greeting (self):
        print("Hello, my name is " + self.name)

    #def Save (self):
    #    print("Saved")

class DB:
    def Save (self, person: Person):
        print(str(person.name) + " saved")

if __name__ == "__main__":
    db = DB()
    ivan = Person("Ivan")
    julia = Person("Julia")
    db.Save(ivan)
    db.Save(julia)

    print("---")


#OCP

class IArea:
    def Area (self):
        pass

class Square(IArea):
    def __init__ (self, width):
        self.width = width
    def Area(self):
        return self.width**2

class Circle(IArea):
    def __init__(self, radius):
        self.radius = radius
    def Area(self):
        return 3.14*self.radius**2

if __name__ == "__main__":
    square = Square(10)
    circle = Circle(10)
    print(square.Area())
    print(circle.Area())

    print("---")


#LSP

class Auto:
    def Power(self):
        pass

class Lexus(Auto):
    def Power(self):
        return 300

class Dodge(Auto):
    def Power(self):
        return 160

def GetPower (car: Auto):
    return car.Power()

if __name__ == "__main__":
    car1 = Lexus()
    car2 = Dodge()
    print(GetPower(car1))
    print(GetPower(car2))

    print("---")


#ISP

#class IShape:
#    def DrawCircle(self):
#        pass
#    def DrawTriangle(self):
#        pass
#
#class Circle(IShape):
#    def DrawCircle(self):
#        #code
#        pass
#    def DrawTriangle(self): Circle is not a triangle
#        pass
#
#class Triangle(ITriangle):
#    def DrawCircle(self): Triangle is not a circle
#        pass
#    def DrawTriangle(self):
#        #code
#        pass

class ICircle:
    def DrawCircle(self):
        pass

class ITriangle:
    def DrawTriangle(self):
        pass

class Circle(ICircle):
    def DrawCircle(self):
        print("Draw Circle")
        pass

class Triangle(ITriangle):
    def DrawTriangle(self):
        print("Draw Triangle")
        pass

if __name__ == "__main__":
    circle = Circle()
    triangle = Triangle()
    circle.DrawCircle()
    triangle.DrawTriangle()

    print("---")



#DIP

class Idb:
    def Connect (self):
        pass

class MySQLDB(Idb):
    def Connect(self):
        print("MySQL DB is connected")

class MongoDB(Idb):
    def Connect(self):
        print("MongoDB is connected")

class Books:
    def __init__ (self, db: Idb):
        self.db = db

    def GetBooks (self):
        conn = self.db.Connect()
        print("List of books")

if __name__ == "__main__":
    mysql = MySQLDB()
    mongo = MongoDB()
    b1 = Books(mysql).GetBooks()
    b2 = Books(mongo).GetBooks()