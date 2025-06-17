# import mysql.connector

# mydb= mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234"


# )

# mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234",
#     database="mydatabase"
# )

# mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE student(name varchar(255), address varchar(255))")


# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234",
#     database="mydatabase"
# )

# mycursor=mydb.cursor()
# spl="INSERT INTO student(name,address) VALUES(%s,%s)"
# val=[("Hanan","Mangalath"),
# ("Afsal","vattathil"),
# ("jiji","kollam"),
# ("jaseer","kochi")]
# mycursor.executemany(spl,val)

# mydb.commit()





# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234",
#     database="mydatabase"
# )

# mycursor=mydb.cursor()
# mycursor.execute("SELECT *FROM student")
# my=mycursor.fetchall()

# for x in my:
#     print(x)

# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234",
#     database="mydatabase"
# )

# mycursor=mydb.cursor()

# sq="SELECT * FROM student WHERE address= 'Mangalath'"
# mycursor.execute(sq)
# my=mycursor.fetchall()

# for x in my:
#     print(x)


# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234",
#     database="mydatabase"
# )

# mycursor=mydb.cursor()

# sq="SELECT * FROM student ORDER BY name"
# mycursor.execute(sq)
# my=mycursor.fetchall()

# for x in my:
#     print(x)


# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234",
#     database="mydatabase"
# )

# mycursor=mydb.cursor()

# sq="DELETE  FROM student WHERE name= 'Hanan'"
# mycursor.execute(sq)
# mydb.commit()


# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root1234",
#     database="mydatabase"
# )

# mycursor=mydb.cursor()

# sq="UPDATE student SET address ='Valli' WHERE address= 'vattathil'"
# mycursor.execute(sq)
# mydb.commit()