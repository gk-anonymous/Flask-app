from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    
    return "Hello, Wordr!"

@app.route('/home')
def home():
    
    return "Hello, welcome to Home Page!"

@app.route('/login')
def Login():
    
    return "Hello, welcome to Login Page!"



if __name__ == "__main__":
    app.run(debug=True)
