from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject	= data['subject']
		message = data['message']
		file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data['email']
		subject	= data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

@app.route('/')
def start():
	return render_template('index.html')

@app.route('/index.html')
def home():
	return render_template('index.html')

@app.route('/project.html')
def project():
	return render_template('project.html')

@app.route('/thankyou.html')
def thankyou():
	return render_template('thankyou.html')


@app.route('/components.html')
def components():
	return render_template('components.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	return 'something went wrong'