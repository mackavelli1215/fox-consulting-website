from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define routes - registers routes to app
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)