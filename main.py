from flask import Flask,request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/", methods=['POST'])
def info():
    template = jinja_env.get_template('index.html')
    template2 = jinja_env.get_template('welcome.html')

    name = request.form['name']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    name_spaces = 0
    for i in range(len(str(name))):
        if name[i] == " ":
            name_spaces = name_spaces + 1

    pass_spaces = 0
    for i in range(len(str(password))):
        if password[i] == " ":
            pass_spaces = pass_spaces + 1

    email_spaces = 0
    email_at = 0
    email_per = 0

    for i in range(len(str(email))):
        if email[i] == " ":
            email_spaces = email_spaces + 1
        if email[i] == "@":
            email_at = email_at + 1
        if email[i] == ".":
            email_per = email_per + 1

    no_match = "    Passwords didn't match!"
    not_long = "    Must be less than 20 characters!"
    too_long = "    Must be more than 3 characters!"
    no_space = "    No spaces allowed!"
    invalid_email = "   Invalid eMail!"

    pass_not = not_long
    pass_too = too_long
    name_not = not_long
    name_too = too_long
    name_np = no_space
    pass_np = no_space
    inv_email = invalid_email

    check = 0
    if (email_spaces == 0)and(email_at == 1)and(email_per == 1):
        inv_email = ""
        check = check + 1
    if name_spaces == 0:
        name_np = ""
        check = check + 1
    if pass_spaces == 0:
        pass_np = ""
        check = check + 1
    if password == verify:
        no_match = ""
        check = check + 1
    if len(password) >= 3:
        pass_too = ""
        check = check + 1
    if len(password) <= 20:
        pass_not = ""
        check = check + 1
    if len(name) >= 3:
        name_too = ""
        check = check + 1
    if len(name) <= 20:
        name_not = ""
        check = check + 1

    if check != 8:
        return template.render(name=name,password=password,verify=verify,
                                email=email,no_match=no_match,
                                pass_not=pass_not,pass_too=pass_too,
                                name_not=name_not,name_too=name_too,
                                name_np=name_np,pass_np=pass_np,
                                inv_email=inv_email)
    else:
        return template2.render(name=name)
app.run()
