from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['# DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <title> User signup </title>
        <style type="text/css">
            form {{
                display: block;
                margin-top: 0em;
                }}
            }}
            table {{
                display: table;
                border-collapse: separate;
                border-spacing: 2px;
                border-color: grey;
            }}
            tbody {{
                display: table-row-group;
                vertical-align: middle;
                border-color: inherit;
                }}
        </style>
    </head>
    <body>
        <h1> Signup </h1>
    <!-- put some stuff into here :) :p -->
        <form action="/hello" method="post" data-version="1.2">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="usr_name">Username </label>
                        </td>
                        <td>
                            <input type="text" id="usr_name" name="User-name"
                                minlength="3" maxlength="20" required/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="passwd">Password (8 character minimum): </label>
                        </td>
                        <td>
                            <input type="password" id="passwd" name="Password"
                                minlength="3" maxlength="20" required/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="confirm_passwd">Confirm Password </label>
                        </td>
                        <td>
                            <input type="password" id="confirm_passwd" name="Confirm-Password"
                                minlength="3" maxlength="20" required/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for "email_address">Email Address (optional): </label>
                        </td>
                        <td>
                            <input type="text" id="email_address" name="Email-Address"/>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit" name="submit query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form



@app.route("/hello", methods=['POST'])
def hello():
    email_name = ""
    user_name = request.form["User-name"] #this takes the number field and converts it into int
    user_password = request.form["Password"] # this takes what is is the text box and passes it to the the variable 
    confirm_password = request.form["Confirm-Password"]
    
    if user_password == confirm_password:
        return '<h1> Welcome, ' + user_name +'</h1>'
    else:
        return '<h1> Passwords do not match, please try again </h1>'
    

    # this calls the rotate_string function from Caesar and passes text and rot as parameters
     # this prints the returned value after the function manipulates the parameters above

    # return encrypted_message  # make sure to return your final variable every time or else it will not do anything. 
     # we do this so that way we can pass an arbitrary value back to {0} as a place holder. 
     
app.run()
