from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, validators, StringField, SubmitField 
from wtforms.validators import ValidationError, DataRequired
from house_info import *
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), validators.Length(min=6, max=35)])
    password = StringField('Password:', validators=[DataRequired(), validators.Length(min=3, max=35)])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('main.html')
    @app.route("/main.html", methods=['GET', 'POST'])
    def main():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            print(name,+  " ",+ email,+ " ", + password)
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('main.html')
    
    
    @app.route("/buy.html", methods=['GET', 'POST'])
    def buy():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            print(name,+  " ",+ email,+ " ", + password)
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('buy.html')
    @app.route("/rent.html", methods=['GET', 'POST'])
    def rent():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            print(name,+  " ",+ email,+ " ", + password)
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('rent.html')
  
    @app.route("/swap.html", methods=['GET', 'POST'])
    def swap():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            print('here')
            min_price=request.form['minprice']
            max_price=request.form['maxprice']
            
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + max_price)
        else:
            flash('Error: All the form fields are required. ')
        
        return render_template('swap.html')
    @app.route("/houselist.html", methods=['GET', 'POST'])
    def houselist():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            print(name,+  " ",+ email,+ " ", + password)
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('houselist.html')
            

            


if __name__ == "__main__":
    app.run(host = "0.0.0.0")

