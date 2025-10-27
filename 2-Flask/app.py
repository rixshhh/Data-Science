from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/") # RULE PARAMETER
def welcome():
    return "Hello, Flask! from VS Code!"

@app.route("/index")
def index():
    return "Welcome to the index page"

# THIS IS THE ENTRY POINT OF ANY (.py) FILE
if __name__=="__main__":
    app.run(debug=True) # MOST IMPORTANT THING