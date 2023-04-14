from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from functions import *


class bmiForm(FlaskForm):
    feet = FloatField('Feet', validators=[InputRequired(), NumberRange(0)])
    inches = FloatField('Inches', validators=[InputRequired(), NumberRange(0, 11)])
    weight = FloatField('Weight', validators=[InputRequired(), NumberRange(0)])
    submit = SubmitField('Calculate')

def create_app():
    '''Creates app'''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    @app.route("/", methods=('GET', 'POST'))
    @app.route("/index", methods=('GET', 'POST'))
    def bmiPage():
        form = bmiForm()
        bmi = 0.0
        category = 'None'
        if form.validate_on_submit():
            feet = form.feet.data
            inches = form.inches.data
            weight = form.weight.data
            height = feet*12 + inches
            if height <= 0:
                flash('Total height must be greater than 0 inches')
            else:
                bmi = bmiCalculator(height, weight)
                category = categorize(bmi)

        return render_template('bmi.html', form=form, bmi=bmi, category=category)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)