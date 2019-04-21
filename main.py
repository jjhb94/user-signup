from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['# DEBUG'] = True

form = ""

    


@app.route("/", methods=['POST'])
def validate():

    email_name = request.form["Email-Address"]
    user_name = request.form["User-name"] #this takes the number field and converts it into int
    username_error =''
    password_error =''

    user_password = request.form["Password"] # this takes what is is the text box and passes it to the the variable 
    confirm_password = request.form["Confirm-Password"]
    
    if (not user_name) or (not is_valid(user_name)) or (' ' in user_name):
        username_error = 'That is not a valid username'
    if (not username_error):
        if user_password != confirm_password:
            password_error = 'that is not a valid password'
        return render_template("add-confirmation.html", valid_credentials=user_name)#'<h1> Welcome, ' + user_name +'</h1>'
       
    else:
        return render_template('index.html', valid_credentials=user_name, invalid_credentials=username_error)



@app.route("/")
def index():
    return render_template("index.html") 

if __name__ == "__main__":
    app.run()
