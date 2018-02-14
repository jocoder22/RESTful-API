"""This is the Python app in Virtual Environment."""


from flask import Flask, jsonify


app = Flask(__name__)


Patients = [
    {
        'name': 'name',
        'Biodata':[
            {
            'sex': 'male',
            'age': 54,
            'race': 'black'
            }
        ]
    }
]


@app.route('/patient', methods=['POST'])
def add_patient():
    pass

@app.route('/patient/<string:name>')
def get_patientInfor(name):
    pass


@app.route('/patients')
def get_allPatients():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
