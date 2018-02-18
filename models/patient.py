"""
This is the file for out patient model.

Models:

"""

from db import db


class PatientModel(db.Model):
    """Docstring for PatientModel.

    Patient Model:

    """

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    sex = db.Column(db.String(80))
    age = db.Column(db.Integer)
    race = db.Column(db.String(80))

    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.id'))
    clinic = db.relationship('ClinicModel')

    def __init__(self, name, sex, age, race, clinic_id):
        """Initialize the class."""
        self.name = name
        self.sex = sex
        self.age = age
        self.race = race
        self.clinic_id = clinic_id

    def json(self):
        """Return json representation of our object."""
        return {'name': self.name, 'sex': self.sex, 'age': self.age,
                'race': self.race}

    @classmethod
    def findPatient(cls, name):
        """Define method on the resource i.e get."""
        return cls.query.filter_by(name=name).first()

    def insertPatient(self):
        """Insert  and update the database."""
        db.session.add(self)
        db.session.commit()

    def deletePatient(self):
        """Will delete patient."""
        db.session.delete(self)
        db.session.commit()
