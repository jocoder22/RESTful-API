"""This is the Python app in Virtual Environment."""


from flask import Flask, jsonify, request

app = Flask(__name__)
Patients = [
    {
        'name': 'James',
        'Biodata': [
            {
             'sex': 'male',
             'age': 44,
             'race': 'black'
            }
        ]
    },
    {
        'name': 'John',
        'Biodata': [
            {
             'sex': 'male',
             'age': 30,
             'race': 'White'
            }
        ]
    },
    {
        'name': 'Jane',
        'Biodata': [
            {
<<<<<<< HEAD
            'sex': 'female',
            'age': 22,
            'race': 'Latino'
=======
             'sex': 'female',
             'age': 21,
             'race': 'Latino'
>>>>>>> 4059339707b0486f639bba367d0175d837488ed7
            }
        ]
    }
]


<<<<<<< HEAD
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
=======
@app.route('/patient/<string:name>', methods=['POST'])
def add_patient(name):
    postdata = request.get_json()
    new_data = {
                    'name': name,
                    'Biodata': [
                        {
                         'sex': postdata['sex'],
                         'age': postdata['age'],
                         'race': postdata['race']
                        }
                    ]
                }
    Patients.append(new_data)
    return jsonify({'Patients': Patients})

>>>>>>> 4059339707b0486f639bba367d0175d837488ed7

@app.route('/patient/<string:name>')
def get_patientInfor(name):
    for patient in Patients:
        if patient['name'] == name:
            return jsonify(patient)
    return 'Patient: {} not found in our patient\'s database'.format(name)


@app.route('/patient/<string:name>/<string:Biodata>')
def get_biodata(name, Biodata):
    for patient in Patients:
        if patient['name'] == name:
            patientbios = patient['Biodata']
            return jsonify({'Biodata': patientbios})
    return 'Patient: {} not found in our patient\'s database'.format(name)


@app.route('/patients')
def get_allPatients():
    return jsonify({'All Patient': Patients})


<<<<<<< HEAD
@app.route('/patient/<string:name>/<string:Biodata>')
def get_biodata(name, Biodata):
    for patient in Patients:
        if patient['name'] == name:
            patientBiodata = patient['Biodata']
            return jsonify({'Biodata': patientBiodata})
    return 'Patient: {} not found in our patient\'s database'.format(name)


=======
>>>>>>> 4059339707b0486f639bba367d0175d837488ed7
if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
