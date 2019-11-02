import mysql.connector

#SRP

class Person:
    def __init__(self, name: str):
        self.name = name

    def greeting(self):
        print("Hello, my name is " + self.name)

    #def save(self):
    #    con = mysql.connector.connect(
    #        host = "localhost",
    #        user = "root",
    #        password = "",
    #        database = "myDatabase",
    #        port = 3306
    #    )
    #    cur = con.cursor()
    #    cur.execute("INSERT INTO persons (ID, NAME) VALUES (NULL, %s)", (self.name))
    #    con.commit()
    #    cur.close()
    #    con.close()

class Database:
    def __init__(self):
        self.con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "database",
            port = 3306
        )

    def save_person(self, person: Person):
        cur = con.cursor()
        cur.execute("INSERT INTO persons (ID, NAME) VALUES (NULL, %s)", (person.name))
        self.con.commit()
        cur.close()
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.con.close()

if __name__ == "__main__":
    with Database() as database: #Here is __init__ was invoked
        ivan = Person("Ivan")
        julia = Person("Julia")
        database.save_person(ivan)
        database.save_person(julia)

        print("---")

        #Here is __exit__ was invoked


#OCP

class IArea:
    def area(self):
        pass

class Square(IArea):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width**2

class Circle(IArea):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2

if __name__ == "__main__":
    square = Square(10)
    circle = Circle(10)
    print(square.area())
    print(circle.area())

    print("---")


#LSP

class Auto:
    def power(self):
        pass

class Lexus(Auto):
    def power(self):
        return 300

class Dodge(Auto):
    def power(self):
        return 160

def get_power(car: Auto):
    return car.power()

if __name__ == "__main__":
    car_1 = Lexus()
    car_2 = Dodge()
    print(get_power(car_1))
    print(get_power(car_2))

    print("---")


#ISP

#class IShape:
#    def draw_circle(self):
#      pass
#    def draw_triangle(self):
#      pass
#
#class Circle(IShape):
#    def draw_circle(self):
#      #code
#      pass
#    def draw_triangle(self): Circle is not a triangle
#      pass
#
#class Triangle(ITriangle):
#    def draw_circle(self): Triangle is not a circle
#      pass
#    def draw_triangle(self):
#      #code
#      pass

class ICircle:
    def draw_circle(self):
        pass

class ITriangle:
    def draw_triangle(self):
        pass

class Circle(ICircle):
    def draw_circle(self):
        print("Draw Circle")
        pass

class Triangle(ITriangle):
    def draw_triangle(self):
        print("Draw Triangle")
        pass

if __name__ == "__main__":
    circle = Circle()
    triangle = Triangle()
    circle.draw_circle()
    triangle.draw_triangle()

    print("---")


#DIP

class IDatabase:
    def connect(self):
      pass

class MySQLDatabase(IDatabase):
    def connect(self):
      print("MySQL Database is connected")

class MongoDatabase(IDatabase):
    def connect(self):
      print("MongoDatabase is connected")

class Books:
    def __init__(self, database: IDatabase):
      self.database = database

    def get_books(self):
      conn = self.database.connect()
      print("List of books")

if __name__ == "__main__":
    mysql = MySQLDatabase()
    mongo = MongoDatabase()
    b1 = Books(mysql).get_books()
    b2 = Books(mongo).get_books()
