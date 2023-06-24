# 1 Importing the flask library
from flask import Flask
# 2 render_template to load html files
from flask import render_template
# 2a request to receive the data from html file(register) to flask(perform registration function)
from flask import request
from my_db import Database
db=Database()
from my_api import API
api=API()

#2b redirect to redirect a webpage to another webpage
from flask import redirect

#2c
from flask import session
#To open other pages only through login and not directly

# 3 creating a flask object
app = Flask(__name__)


# Main page
@app.route("/")
def index():
    return render_template("login.html")


# Regitration page
@app.route("/register")
def register():
    return render_template("register.html")


# Function to perform registration
@app.route("/perform_registration", methods=["post"])
def perform_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    res = db.insert_entry(name, email, password)
    if res:
        return render_template('login.html',message="Success, Registered Successfully!!!.You can login now.")
    else:
        return render_template('register.html',message="Email Already exists!!/Enter valid email..")


@app.route("/perform_login" ,methods=["post"])
def perform_login():
    email = request.form.get("email")
    password = request.form.get("password")
    response=db.check_login(email,password)
    if response:
        return redirect("/profile")
    else:
        return render_template('login.html',message="Email doesn't exist!!,Please login again..")

@app.route("/profile")
def profile():
        return render_template("profile.html")


@app.route("/sen")
def sen():
        return render_template("sentiment.html")


@app.route("/perform_sen",methods=['post'])
def perform_sen():
        text=request.form.get("sen_text")
        response=api.perform_sentiment(text)
        print(response)
        return render_template("sentiment.html",response=response)

@app.route("/tax")
def tax():
        return render_template("taxonomy.html")


@app.route("/perform_tax",methods=['post'])
def perform_tax():
        text=request.form.get("tax_text")
        response=api.perform_taxonomy(text)
        print(response)
        return render_template("taxonomy.html",response=response)

@app.route("/pe")
def pe():
        return render_template("pe.html")


@app.route("/perform_pe",methods=['post'])
def perform_pe():
        text=request.form.get("pe_text")
        response=api.perform_pe(text)
        print(response)
        return render_template("pe.html",response=response)

@app.route("/goback",methods=["post"])
def go_back():
    return redirect("/profile")





# Run the website ,debug =true for automatically invoking changes with running again and again
app.run(debug=True)
