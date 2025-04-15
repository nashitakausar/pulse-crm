# test_db.py
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="CRM_user",
    password="nash1912",
    database="simple_crm"
)

print("Connected successfully!")

cursor = db.cursor()
cursor.execute("SELECT 1;")
print(cursor.fetchone())
