from flask import Flask,render_template,request,url_for,redirect,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Database@122'
app.config['MYSQL_DB'] = 'hmsys'
mysql = MySQL(app)


@app.route('/')
def hello():
	return render_template('welcome.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST'])
def submit_form():
	msg=''
	if request.method == 'POST':
		username = request.form['username']
		email=request.form['email']
		passwd = request.form['passwd']
		cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cur.execute("SELECT  * FROM users WHERE username=%s AND email = %s AND passwd = %s",(username,email,passwd))
		account = cur.fetchone()
		if account:
			session['loggedin']=True
			session["user"]=account["username"]
			return redirect('recepD')
		else:
			msg = 'Incorrect username/password!'
			return render_template('login.html',msg=msg)

@app.route("/recepD")
def dashboard():
	if('user' in session):
		return render_template("recepD.html")
	else:
		return render_template('login.html')


#this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
	#print("hellooooooooooooo")
	session.pop("user",None)
	session.clear()
	# Redirect to login page
	return redirect('login.html')

@app.route('/viewPr')
def indexP():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM patient")
	data = cur.fetchall()
	cur.close()
	return render_template('viewP.html',patients=data)

@app.route('/updateP',methods=['POST','GET'])
def update():
	if request.method == 'POST':
		id_data = request.form['id']
		name = request.form['name']
		gender = request.form['gender']
		age = request.form['age']
		email = request.form['email']
		phone = request.form['phone']

		cur = mysql.connection.cursor()
		cur.execute("""
					UPDATE patient SET p_name=%s,gender=%s,age=%s,email=%s,phone_no=%s 
					where patient_id=%s """,(name,gender,age,email,phone,id_data))
		mysql.connection.commit()
		return redirect('viewPr')

@app.route('/deleteP/<int:id_data>',methods=['GET'])
def deleteP(id_data):
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM patient WHERE patient_id=%s",(id_data,))
	mysql.connection.commit()
	return redirect('viewPr')

@app.route('/departments')
def indexDp():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM Departments")
	data = cur.fetchall()
	cur.close()
	return render_template('dept.html',department=data)

@app.route('/docList')
def indexD():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM Doctor")
	data = cur.fetchall()
	cur.close()
	return render_template('viewD.html',doctors=data)

@app.route('/updateD',methods=['POST','GET'])
def updateD():
	if request.method == 'POST':
		id_data = request.form['id']
		name = request.form['name']
		gender = request.form['gender']
		age = request.form['age']
		email = request.form['email']
		phone = request.form['phone']
		department=request.form['department']
		salary = request.form['salary']
		cur = mysql.connection.cursor()
		cur.execute("""
					UPDATE Doctor SET doc_name=%s,d_gender=%s,age=%s,email=%s,phone_no=%s,department=%s,salary=%s
					where doc_id=%s """,(name,gender,age,email,phone,department,salary,id_data))
		mysql.connection.commit()
		return redirect('docList')
		
@app.route('/addDoc')
def depts():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM Departments")
	data = cur.fetchall()
	cur.close()
	print(data)
	return render_template('addD.html',dpt=data)

	
@app.route('/insertD',methods=['POST'])
def insertD():
	if request.method== 'POST':
		name = request.form['name']
		gender = request.form['gender']
		age = request.form['age']
		email = request.form['email']
		phone = request.form['phone']
		department=request.form['department']
		salary = request.form['salary']
		cur = mysql.connection.cursor()
		cur.execute("insert into doctor(doc_name,d_gender,age,email,phone_no,department,salary) values(%s,%s,%s,%s,%s,%s,%s)",(name,gender,age,email,phone,department,salary))
		mysql.connection.commit()
		return redirect('docList')

@app.route('/insertP',methods=['POST'])
def insertP():
	if request.method== 'POST':
		name = request.form['name']
		gender = request.form['gender']
		age = request.form['age']
		email = request.form['email']
		phone = request.form['phone']
		cur = mysql.connection.cursor()
		cur.execute("insert into Patient(p_name,gender,age,email,phone_no) values(%s,%s,%s,%s,%s)",(name,gender,age,email,phone))
		mysql.connection.commit()
		return redirect('viewPr')

@app.route('/addDept')
def addDepartment():
	return redirect('AddDept.html')
		
@app.route('/scheduleList')
def indexsch():
	cur=mysql.connection.cursor()
	cur.execute("""select app_id, d.doc_name,p.p_name,app_date from 
					appointment as a 
					inner join 
					doctor as d 
					inner join patient as p 
					where a.doc_id=d.doc_id and a.patient_id=p.patient_id;""")
	data = cur.fetchall()
	cur1=mysql.connection.cursor()
	cur1.execute("SELECT * FROM doctor")
	doc = cur1.fetchall()
	cur2=mysql.connection.cursor()
	cur2.execute("SELECT * FROM patient")
	pat=cur2.fetchall()
	cur.close()
	cur1.close()
	cur2.close()
	return render_template('viewsch.html',lists=data,dlist=doc,plist=pat)

@app.route('/schedule')
def schedule():
	cur=mysql.connection.cursor()
	cur1=mysql.connection.cursor()
	cur.execute("SELECT * FROM doctor")
	doc = cur.fetchall()
	cur1.execute("SELECT * FROM patient")
	pat=cur1.fetchall()
	cur.close()
	cur1.close()
	return render_template('sche.html',dlist=doc,plist=pat)

@app.route('/scheApp',methods=['POST'])
def scheApp():
	if request.method== 'POST':
		doctor = request.form['doctor']
		patient = request.form['patient']
		print(doctor)
		print(patient)
		date = request.form['date']
		cur = mysql.connection.cursor()
		cur.execute("insert into Appointment(patient_id,doc_id ,app_date) values(%s,%s,%s)",(patient,doctor,date))
		mysql.connection.commit()
		return redirect('scheduleList')

@app.route('/insertDpt',methods=['POST'])
def insertDpt():
	if request.method== 'POST':
		name = request.form['name']
		treatment = request.form['treatment']
		cur = mysql.connection.cursor()
		cur.execute("insert into Departments(department,treatment) values(%s,%s)",(name,treatment))
		mysql.connection.commit()
		return redirect('departments')

@app.route('/deptDoc/<string:page_name>',methods=['POST','GET'])
def deptDoc(page_name):
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM Doctor where department =%s ",(page_name,))
	data = cur.fetchall()
	cur.close()
	return render_template('viewD.html',doctors=data)

@app.route('/deleteSche/<int:id_data>',methods=['GET'])
def deleteSche(id_data):
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM Appointment WHERE app_id=%s",(id_data,))
	mysql.connection.commit()
	return redirect('/scheduleList')

@app.route('/updatesch',methods=['POST','GET'])
def updatesch():
	if request.method == 'POST':
		id_data = request.form['id']
		doctor = request.form['doctor']
		patient = request.form['patient']
		date =request.form['date']
		cur = mysql.connection.cursor()
		cur.execute("UPDATE Appointment SET patient_id=%s,doc_id=%s,app_date=%s where app_id=%s",(patient,doctor,date,id_data))
		mysql.connection.commit()
		return redirect('scheduleList')


if __name__ == '__main__':
    app.run(port=5000,debug=True)