#!C:/Program Files/Python39
print("Content-Type:text/html")
print()

import cgi

print("<h1> Registratio Form</h1>")
print("<hr/")
print("<h1> Using input tag</h1>")
print("<body bgcolo='red'>")

form = cgi.FieldStorage()

Firstname = form.getvalue("Firstname")
Lastname = form.getvalue("Lastname")
Phonenumber = form.getvalue("Number")
Email = form.getvalue("Email")
Gender = form.getvalue("Gender")
Password = form.getvalue("Pass")

import mysql.connector

con = mysql.connector.connect(user="", password="", host="127.0.0.1", database="data")
cur = con.cursor()

cur.execute("insert user values(%s,%s,%s,%s,%s,%s)",(Firstname,Lastname,Phonenumber,Email,Gender,Password))
con.commit()

cur.close()
con.close()
print("<h3>Information inserted Successfully</h3>")