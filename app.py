from flask import Flask, request, render_template

import forms.classForm, forms.characterForm
import getChosenClass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/class')
def classPicker():
    form = forms.classForm.ClassForm()
    if form.validate_on_submit():
        selected_class = form.className.data
        # do something with the selected class
    return render_template('classForm.html', form=form)

@app.route('/character', methods=['POST'])
def character():
    className = request.form['className']
    # print('You have chosen ' + className)
    classData = getChosenClass.main(className.lower())

    # print(classData)
    
    automaticProficiencyObjects = classData['proficiencies']
    automaticProficiencies = []
    for item in automaticProficiencyObjects:
        automaticProficiencies.append(item['name'])

    # print(automaticProficiencies)

    data = {'dndClass': className }
    form=forms.characterForm.CharacterForm(data=data)
    # form.dndClass = className
    form.proficiencies.choices = automaticProficiencies
    # proficiencyOptions = classData['proficiency_choices']
    # automaticStartingEquipment = classData['starting_equipment']
    # startingEquipmentChoices = classData['starting_equipment_options'][0]['options']
    # print(automaticStartingEquipment)

    # form=forms.characterForm.CharacterForm(data=data)
    #form=forms.characterForm.CharacterForm(obj={'dndClass': className, 'proficiencies': automaticProficiencies })
    
    if form.validate_on_submit():
        # handle form submission
        pass

    return render_template('characterForm.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
