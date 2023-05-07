from flask import Flask, request, render_template
from requests import api

import forms.classForm, forms.characterForm
import getChosenClass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return render_template('home.html')

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
    classData = getChosenClass.main(className.lower())
    
    automaticProficiencyObjects = classData['proficiencies']
    automaticProficiencies = []
    for item in automaticProficiencyObjects:
        automaticProficiencies.append(item['name'])

    apiProficiencyOptions = classData['proficiency_choices'][0]
    proficiencyOptions = []
    for item in apiProficiencyOptions['from']['options']:
         proficiencyOptions.append(item['item']['name'])

    apiStartingEquipment = classData['starting_equipment']
    startingEquipment = []
    for item in apiStartingEquipment:
        startingEquipment.append(item['equipment']['name'])

    apiEquipmentOptions = classData['starting_equipment_options']
    equipmentOptions = []
    for item in apiEquipmentOptions:
        print(item)
        equipmentOptions.append(item['desc'])

    data = {'dndClass': className }
    form=forms.characterForm.CharacterForm(data=data)

    form.automaticProficiencies.choices = automaticProficiencies
    form.proficiencyChoices.choices = proficiencyOptions
    form.autoStartingEquipment.choices = startingEquipment
    form.equipmentOptions.choices = equipmentOptions

    # automaticStartingEquipment = classData['starting_equipment']
    # startingEquipmentChoices = classData['starting_equipment_options'][0]['options']
    # print(automaticStartingEquipment)

    # form=forms.characterForm.CharacterForm(data=data)
    # form=forms.characterForm.CharacterForm(obj={'dndClass': className, 'proficiencies': automaticProficiencies })
    
    if form.validate_on_submit():
        # handle form submission
        pass

    return render_template('characterForm.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
