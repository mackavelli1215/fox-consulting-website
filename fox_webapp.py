from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)


# Define routes - registers routes to app
@app.route('/')
def home():
  return render_template('home.html')


@app.route('/client')
def client():
  return render_template('client.html')


@app.route('/staff')
def staff():
  return render_template('staff.html')


# Start the app
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
