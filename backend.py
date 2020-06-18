import sqlite3

class Database:

    def __init__(self,db): #constructor
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text, author text,year integer, isbm integer)")
        self.conn.commit()


    def insert(self,title,author,year,isbm):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbm))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbm=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbm=?",(title,author,year,isbm))
        rows=self.cur.fetchall()
        return rows

    def update(self,title,author,year,isbm,id):
        self.cur.execute("UPDATE  book SET title=?, author=?,  year=?, isbm=? WHERE id=?",(title,author,year,isbm,id))
        self.conn.commit()



    def delete(self,id):
        self.cur.execute("DELETE FROM  book WHERE id=?",(id,))
        self.conn.commit()

    def __del__(self): #destructor
        self.conn.close()


    #connect()
    #insert("The Sun","Smith",1919,93)
    #update("the moon","John",1920,94,3)
    #delete(2)
    #print(view())
    #print(search(author="payal"))
