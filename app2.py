"""This is the Python app in Virtual Environment."""


from flask import Flask, jsonify


app = Flask(__name__)


Patients = [
    {
        'name': 'James',
        'Biodata':[
            {
            'sex': 'male',
            'age': 44,
            'race': 'black'
            }
        ]
    },
    {
        'name': 'John',
        'Biodata':[
            {
            'sex': 'male',
            'age': 30,
            'race': 'White'
            }
        ]
    },
    {
        'name': 'Jane',
        'Biodata':[
            {
            'sex': 'female',
            'age': 22,
            'race': 'Latino'
            }
        ]
    }
]


@app.route('/patient', methods=['POST'])
def add_patient():
    inputData = request.get_json()
    new_data = {
        'name': inputData['name'],
        'Biodata':[
            {
            'sex': inputData['sex'],
            'age': inputData['age'],
            'race': inputData['race']
            }
        ]
    }
    Patients.append(new_data)
    return jsonify(new_data)
    # return jsonify({'All Patient': Patients})

@app.route('/patient/<string:name>')
def get_patientInfor(name):
    for patient in Patients:
        if patient['name'] == name:
            return jsonify(patient)
    return 'Patient: {} not found in our patient\'s database'.format(name)


@app.route('/patients')
def get_allPatients():
    return jsonify({'All Patient': Patients})


@app.route('/patient/<string:name>/<string:Biodata>')
def get_biodata(name, Biodata):
    for patient in Patients:
        if patient['name'] == name:
            patientBiodata = patient['Biodata']
            return jsonify({'Biodata': patientBiodata})
    return 'Patient: {} not found in our patient\'s database'.format(name)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
