from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html', title="Signup")

@app.route('/', methods=['POST', 'GET'])
def check_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    if not check_name(username):
        username_error = 'Not a valid username'
        error = True
    if not check_name(password):
        password_error = 'Not a valid password'
        error = True
    if not verify_pass(password, verify):
        verify_error = 'Passwords do not match'
        error = True
    if not check_email(email):
        email_error = 'Not a valid email'
        error = True

    if not error:
        return redirect("/welcome?query=" +username)

    return render_template('index.html', title="Signup",
                           username=username, email=email,
                           username_error=username_error, password_error=password_error,
                           verify_error=verify_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


def check_name(name):
    if len(name) < 3 or len(name) > 20 or name.count(' ') > 0:
        return False
    return True

def check_email(mail):
    if mail == '':
        return True
    if mail.count('@') == mail.count('.') == 1 and check_name(mail):
        return True
    return False

def verify_pass(password,verify):
    if password == verify:
        return True
    return False


app.run()