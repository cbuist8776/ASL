from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method == 'POST':
		fname = request.form['fname']
		
		return render_template('age.html', fname=fname)

	return render_template('index.html')

if __name__=='__main__':
	app.run()