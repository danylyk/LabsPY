#SRP

class Person:
    def __init__(self, name: str):
        self.name = name

    def Greeting (self):
        print("Hello, my name is " + self.name)

    #def Save (self):
    #    pass

class DB:
    def Save (person: Person):
        pass



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

def GetPower (car):
    car.Power()


#ISP

class ICircle:
    def DrawCircle(self):
        pass

class ITriangle:
    def DrawTriangle(self):
        pass

class Circle(ICircle):
    def DrawCircle(self):
        #code
        pass

class Triangle(ITriangle):
    def DrawTriangle(self):
        #code
        pass



#DIP

class IConnection:
    def Connect (self):
        pass

class MySQLConnect(IConnection):
    def Connect(self):
        pass

class Books:
    def __init__ (self, connection: IConnection):
        pass