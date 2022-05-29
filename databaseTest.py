import mysql.connector

conn = mysql.connector.connect(username='root', password='root',database='face_recognition')
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()