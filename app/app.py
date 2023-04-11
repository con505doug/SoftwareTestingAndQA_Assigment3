from functions import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
@app.route("/index", methods=('GET', 'POST'))
def bmiPage():
    feet = request.form.get('feet')
    inches = request.form.get('inches')
    weight = request.form.get('weight')
    print(feet)
    return render_template('bmi.html') #bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)



