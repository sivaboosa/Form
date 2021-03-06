from html.entities import html5
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder = "template")


mysql = MySQL(app)

@app.route("/", methods = ['GET','POST'])

def registration():
    if request.method == 'POST':
        #Fetch form data
        userdetails = request.form.values
        Firstname = userdetails["Firstname"]
        Lastname = userdetails['Lastname']
        Email = userdetails['Email']   
        Phonenumber = userdetails['Number']
        Password = userdetails['Pass']
        Gender = userdetails['Gender']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO registration(Firstname, Lastname, Email, Phonenumber, Password, Gender) VALUES(%s, %s, %s, %s, %s, %s)",(Firstname, Lastname, Email, Phonenumber, Password, Gender))
        mysql.connection.commit()
        cur.close()
        return redirect('success.html')
    return render_template('form.html')
 
@app.route('/success')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM registration")
    if resultValue > 0:
        userdetails = cur.fetchall()
        return render_template('success.html', userdetails = userdetails)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
