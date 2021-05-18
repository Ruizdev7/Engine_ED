import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123qweAs*",
    database="DB_ENGINE_ED"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM tblRoles")
result = cursor.fetchall()

for i in result:
    print(i)
