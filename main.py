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
    <!-- put some stuff into here :) -->
        <form method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="Usrname">Username </label>
                        </td>
                        <td>
                            <input type="text" id="usr_name" name="Username"/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="passwd">Password (password must be between 3 and 20 characters): </label>
                        </td>
                        <td>
                            <input type="password" id="passwd" name="Password"
                                pattern=".{3,20}" required/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="confirm_passwd">Confirm Password </label>
                        </td>
                        <td>
                            <input type="password" id="confirm_passwd" name="Confrim Password"
                                pattern=".{3,20}" required/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for "email_address">Email Address (optional): </label>
                        </td>
                        <td>
                            <input type="text" id="email" name="Email Address"/>
                        </td>
                    </tr>
                <tbody>
            </table>
            <input type="submit" name="submit query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form["rot"] #this takes the number field and converts it into int
    text = request.form["text"] # this takes what is is the text box and passes it to the the variable 

    new_message = rotate_string(text, int(rot))  # this calls the rotate_string function from Caesar and passes text and rot as parameters
    encrypted_message =  new_message # this prints the returned value after the function manipulates the parameters above

    # return encrypted_message  # make sure to return your final variable every time or else it will not do anything. 
    return form.format(encrypted_message) # we do this so that way we can pass an arbitrary value back to {0} as a place holder. 
app.run()
