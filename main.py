from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['# DEBUG'] = True

form = ""


@app.route("/user", methods=['POST'])
def hello():

    email_name = ""
    user_name = request.form["User-name"] #this takes the number field and converts it into int
    user_password = request.form["Password"] # this takes what is is the text box and passes it to the the variable 
    confirm_password = request.form["Confirm-Password"]
    
    if user_password != confirm_password:
        return '<h1> Passwords do not match, please try again </h1>'
    return render_template("add-confirmation.html", valid_credentials=user_name)#'<h1> Welcome, ' + user_name +'</h1>'
    


@app.route("/")
def index():
    return render_template("index.html")

app.run()
