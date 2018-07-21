from flask import Flask, render_template
from random import randint


app = Flask(__name__)
@app.route('/')
def loadPage():
	return render_template('page.html')

if __name__ == '__main__':
	app.run(port = 4000, debug=True)