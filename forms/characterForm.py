from flask_wtf.form import FlaskForm
from wtforms.fields.choices import SelectField, SelectMultipleField
from wtforms.fields.simple import StringField

class CharacterForm(FlaskForm):
    characterName = StringField('Name')
    dndClass = StringField('Class', default='', render_kw={'disabled': True})
    # race = SelectField('Race')
    # hitDie = StringField('Hit Die')
    automaticProficiencies = SelectMultipleField('Automatic Proficiencies', choices=[], render_kw={'disabled': True})
    proficiencyChoices = SelectMultipleField('Proficiency Choices')

    # savingThrows = SelectMultipleField('Saving Throws')
    autoStartingEquipment = SelectMultipleField('Automatic Starting Equipment', choices=[], render_kw={'disabled': True})
    equipmentOptions = SelectMultipleField('Equipment Choices', choices=[])
