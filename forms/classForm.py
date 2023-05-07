from flask_wtf.form import FlaskForm
from wtforms.fields.choices import SelectField
import getClasses

class ClassForm(FlaskForm):
    classNames = []
    for item in getClasses.main():
        classNames.append(item['name'])

    className = SelectField('Select a class', choices=classNames)