from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello world'
@app.route('/about')
def about():
	return 'This is test Flask application created by Kate Beliankova '
app.run()