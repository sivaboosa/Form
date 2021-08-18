from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])

def hello():
    if request.method == 'POST':
        #Fetch form data
        userDetails = request.form
        Firstname = userDetails.getvalue("Firstname")
        Lastname = userDetails.getvalue("Lastname")
        Email = userDetails.getvalue("Email")
        Phonenumber = userDetails.getvalue("Number")
        Password = userDetails.getvalue("Pass")
        Gender = userDetails.getvalue("Gender")
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s, %s, %d, %s, %s)",(Firstname, Lastname, Email, Phonenumber, Password, Gender))
        mysql.connection.commit()
        cur.close()
        return redirect('/success')
    return render_template('form.html')
 
@app.route('/registration')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('success.html',userDetails = userDetails)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
