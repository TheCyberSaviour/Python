from flask import Flask
app = Flask(__name__)       # Create a Flask app
@app.route('/')              # Create a route
def hello_world():           # Create a function
    return 'Hello, World!'  # Return a string
if __name__ == '__main__':   # Run the app
    app.run()                # Run the app 
    
#The code above creates a simple Flask app that returns the string “Hello, World!” when you visit the root URL.