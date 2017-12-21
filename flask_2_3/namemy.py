from flask import Flask
app = Flask(__name__)

@app.route('/shiyanlou/')
def hello_world():
	return 'Quesiter'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
