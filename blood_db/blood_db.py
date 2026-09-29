import mysql.connector
class Donor:
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='Anagha',host='localhost',database='blood_db')

        self.c=self.con.cursor()
        print("successfully connected")

    def create(self,name,blood_group,phone,city,last_donation):
        query = 'insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)'
        data = (name,blood_group,phone,city,last_donation)
        self.c.execute(query, data)
        self.con.commit()

    def list(self):
        # Reading all records from db file
        query = 'select * from donor'
        self.c.execute(query)
        record = self.c.fetchall()
        if record:
            # for row in record:
            #     print(row)
            return record
        else:
            print('No Record Found')


    def retrieve(self,id):

        query="select * from donor where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()

        if record:
            return record
        else:
            print("No Record Found")

    def update(self, id, name, blood_group, phone, city, last_donation):
        query = "update donor set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s"

        data = (name, blood_group, phone, city, last_donation, id)


        self.c.execute(query, data)

        self.con.commit()

        if self.c.rowcount > 0:
           return True
        else:
           return False



    def delete(self,id):
        query = "delete from donor where id=%s"

        data=(id,)

        self.c.execute(query, data)

        self.con.commit()

        if self.c.rowcount > 0:
            return True
        else:
            return False


# c=Donor()
# c.create("Anagha","A+","7025870228","kochi","2026-08-10")
# c.list()
# c.retrieve()
# c.delete()
# c.update("Pooja","B+","6789564356","kottayam","2026-11-9")