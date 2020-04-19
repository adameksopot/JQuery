from flask import Flask, render_template, request, jsonify
import re
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():


	name = request.form['name']

	if  re.match("\d{2}-\d{3}", name) :
			return jsonify({'name' : 'Kod pocztowy jest prawidłowy!'})
	else:
			return jsonify({'error' : 'Kod pocztowy jest nieprawidłowy!'})

if __name__ == '__main__':
	app.run(debug=True)