#!C:/Program Files/Python39/python
print("Content-Type:text/html")
print()

import cgi

print("<h1> Registratio Form</h1>")
print("<hr/")
print("<h1> Using input tag</h1>")
print("<body bgcolor='red'>")

form = cgi.FieldStorage()

Firstname = form.getvalue("Firstname")
Lastname = form.getvalue("Lastname")
Email = form.getvalue("Email")
Phonenumber = form.getvalue("Number")
Password = form.getvalue("Password")
Gender = form.getvalue("Gender")

import mysql.connector

con = mysql.connector.connect(user="sid", password="Userpassword", host="localhost", database="test")
cur = con.cursor()

cur.execute("insert user values(%s,%s,%s,%s,%s,%s)",(Firstname,Lastname,Email,Phonenumber,Password,Gender))
con.commit()

cur.close()
con.close()
print("<h3>Information inserted Successfully</h3>")