class Database:
    def connect (self):
        pass

class DatabaseMYSQL(Database):
    def connect(self):
        return "MySQL"

class DatabaseMONGO(Database):
    def connect(self):
        return "MongoDB"

class Books:
    def __init__ (self, database: Database):
        self.database = database

    def get_books (self):
        conn = self.database.connect()
        print("List of books from " + conn)

if __name__ == "__main__":
    mysql = DatabaseMYSQL()
    mongo = DatabaseMONGO()

    books_mysql = Books(mysql)
    books_mongo = Books(mongo)

    books_1 = books_mysql.get_books()
    books_2 = books_mongo.get_books()
