from flask import Flask, render_template, redirect, url_for, flash
import connexion
from forms import *
import database
import BMI
import EmailVerifier
from json2html import *

options = {"swagger_ui": True}

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='./', options=options)

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

app.app.config["SECRET_KEY"] = '5accdb11b2c10a78d7c92c5fa102ea77fcd50c2058b00f6e'

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/post-bmi', methods=['GET', 'POST'])
def bmi():
    form = BMIForm()
    if form.validate_on_submit():
        ret = BMI.DoBMI(form.footField.data, form.inchesField.data, form.poundsField.data)
        flash(ret)
    return render_template('bmi.html', title='Calculate BMI', form=form)

@app.route('/get-bmi', methods=['GET'])
def get_bmi():
    table = database.readBMI()
    return json2html.convert(json=table)
    
@app.route('/post-email', methods=['GET', 'POST'])
def email():
    form = EmailForm()
    if form.validate_on_submit():
        ret = EmailVerifier.Verify(form.email.data)
        flash(ret)
    return render_template('email.html', title='Verify Email', form=form)

@app.route('/get-email', methods=['GET'])
def get_email():
    table = database.readEmailVerifier()
    return json2html.convert(json=table)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)