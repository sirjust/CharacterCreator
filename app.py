from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField

import json
import getClasses

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return 'Hello, World!'

class ClassForm(FlaskForm):
    classesFromAPI = getClasses.main()
    print(classesFromAPI)
    classNames = []
    for item in classesFromAPI:
        classNames.append(item['name'])

    className = SelectField('Select a class', choices=classNames)

@app.route('/class')
def classPicker():
    form = ClassForm()
    if form.validate_on_submit():
        selected_class = form.className.data
        # do something with the selected class
    return render_template('classForm.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
