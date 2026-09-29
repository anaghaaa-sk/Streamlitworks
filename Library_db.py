import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='Anagha',host='localhost',database='library_db')

        self.c=self.con.cursor()
        print("successfully connected")

    def list(self):
        #Reading all records from db file
        query ='select * from book'
        self.c.execute(query)
        record =self.c.fetchall()
        if record:
            for row in record:
                print(row)
        else:
            print('no record found')



    def create(self,title,author,price,language,pages):
            #creating a new records
            query ='insert into book(title,author,price,language,pages) values(%s,%s,%s,%s,%s)'
            data = (title,author,price,language,pages)
            self.c.execute(query, data)
            self.con.commit()



    def retrieve(self,id):

        query="select * from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()

        if record:
            print(record)
        else:
            print("No Record Found")


    def delete(self,id):
        query = "delete from book where id=%s"

        data=(id,)

        self.c.execute(query, data)

        self.con.commit()

        if self.c.rowcount > 0:
            print("Data is deleted")
        else:
            print("No Record Found")


    def update(self,id,title,author,price,language,pages):
        query = "update book set id=%s,title=%s,author=%s,price=%s,language=%s,pages=%s"

        data=(id,title,author,price,language,pages)

        self.c.execute(query, data)

        self.con.commit()

        if self.c.rowcount > 0:
            print("updated successfully")
        else:
            print("No Record Found")


b=BookListCreateRetrieveUpdateDelete()
# b.list()
# b.create('ABC','John',300,'English',500)
# b.retrieve(2)
# b.delete(5)
b.update(6,'BCD','Joy',289,'Hindi',700)