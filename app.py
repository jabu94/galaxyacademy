from flask import Flask, render_template, flash, redirect, url_for, session, logging

# from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# from passlib.hash  import sha256_crypt


app = Flask(__name__)



#1 app.config['MYSQL_HOST'] = 'localhost'
#2 app.config['MYSQL_USER'] = 'root'
#3 app.config['MYSQL_PASSWORD'] = ''
#4 app.config['MYSQL_DB'] = 'galaxy'
#5 app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#initialiseMySQL
#6 mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('.html')

#7 @app.route('/about')
#8 def about():
#9    return render_template('about.html')

#Registration OF The Adminstrator
 class RegisterAdminForm(form)
#11    name = StringField ('Name', [validators.Length(min=1, max=50)])
#12    surname = StringField('Surname', [validators.Length(min=4, max=25)])
#13    dob = DateField('Date Of Birth', [validators])
#14    email = StringField('Email Address', [validators.Length(min=4, max=30)])
#15    address = TextAreaField('Physical Address'), [validators.Length(min=4, max=30)])
#16    contact = IntegerField('Contact Number'), [validators]
#17    role = RadioField ('Role')
#18    dateJoined = DateField('Date Joined Galaxy',)
#19    password = PasswordField('Password', [
#20        validators.DataRequired(),
#21        validators.EqualTo('confirm', message= 'Passwords do not match')
#22    ])
#23    confirm = PasswordField('Confirm Password')
#24    img =


#25 @app.route('/register', methods=['GET', 'POST'])
#26    def registerAdmin():
#27    form = RegisterAdminForm(request.form)
#28    if request.method == 'POST' and form.validate():
#29        name = form.name.data
#30        surname = form.surname.data
#31        dob = form.dob.data
#32        email = form.email.data
#33        address = form.address.data
#34        contact = form.contact.data
#35        role = form.role.data
#36        dateJoined = form.dateJoined.data
#37        password = sha256_crypt.encrypt(str(form.password.data))
#38        img = form.img.data

        #Cursor Creation
#39        cur = mysql.connection.cursor()

#40        cur.execute("INSERT INTO Admin(name, surname, dob, email, address, contact, role, dateJoined, password, img )
#41                    VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)", (name, surname, dob, email, address, contact, role, dateJoined, password, img)  )

        #Commit to DB
#42        mysql.connection.commit()

        #close connection
#43        cur.close()

#44        flash('You are now registered and can log in', 'success')

#45           return render_template('registerAdmin.html')
#46        return render_template('registerAdmin.html', form=form)
    # UserLogin and Access Control Tutorial3
#47    @app.route('/login', method=['GET', 'POST'])
#48        def login():
#49            if request.method == 'POST'
                #Get form Fields
#50                email= request.form['user email']
#51                password_admin = request.form['password']
            #


#51   return render_template('login.html')



if __name__ == '__main__':

    app.debug = True
    app.run()
