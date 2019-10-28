import dependency_injector.containers as containers
import dependency_injector.providers as providers

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


"""the creation of a Books requires additional code to specificaty its dependencies"""
if __name__ == "__main__":
    mysql = MySQLDB()
    mongo = MongoDB()
    b1 = Books(mysql).GetBooks()
    b2 = Books(mongo).GetBooks()


"""So, we can make in other way"""

class DataBases(containers.DeclarativeContainer):
    mysql = providers.Factory(MySQLDB)
    mongo = providers.Factory(MongoDB)

class CBooks(containers.DeclarativeContainer):
    mysql = providers.Factory(Books, db=DataBases.mysql)
    mongo = providers.Factory(Books, db=DataBases.mongo)

if __name__ == '__main__':
    books_mysql = CBooks.mysql()
    books_mongo = CBooks.mongo()