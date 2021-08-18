from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder = "template")


mysql = MySQL(app)

@app.route('/form', methods=['GET','POST'])

def hello():
    if request.method == 'POST':
        #Fetch form data
        userdetails = request.form
        Firstname = userdetails['Firstname']
        Lastname = userdetails['Lastname']
        Email = userdetails['Email']   
        Phonenumber = userdetails['Number']
        Password = userdetails['Pass']
        Gender = userdetails['gender']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s, %s, %d, %s, %s)",(Firstname, Lastname, Email, Phonenumber, Password, Gender))
        mysql.connection.commit()
        cur.close()
        return redirect('/registration')
    return render_template('form.html')
 
@app.route('/success')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('success.html',userDetails = userDetails)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
