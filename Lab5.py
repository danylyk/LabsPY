import mysql.connector

#SRP

class Person:
    def __init__(self, name: str):
        self.name = name

    def Greeting (self):
        print("Hello, my name is " + self.name)

    #def Save (self):
    #    con = mysql.connector.connect(
    #        host = "localhost",
    #        user = "root",
    #        password = "",
    #        database = "mydb",
    #        port = 3306
    #    )
    #    cur = con.cursor()
    #    cur.execute("INSERT INTO persons (ID, NAME) VALUES (NULL, %s)", (self.name))
    #    con.commit()
    #    cur.close()
    #    con.close()

class DB:
    def __init__ (self):
        self.con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "mydb",
            port = 3306
        )

    def SavePerson (self, person: Person):
        cur = con.cursor()
        cur.execute("INSERT INTO persons (ID, NAME) VALUES (NULL, %s)", (person.name))
        self.con.commit()
        cur.close()

    def __exit__ (self):
        self.con.close()

if __name__ == "__main__":
    db = DB()
    ivan = Person("Ivan")
    julia = Person("Julia")
    db.SavePerson(ivan)
    db.SavePerson(julia)

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