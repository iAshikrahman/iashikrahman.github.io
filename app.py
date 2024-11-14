from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, redirect, url_for, flash

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process form data here (e.g., save to database, send email, etc.)
    flash("Message sent successfully!")
    return redirect(url_for('home'))
