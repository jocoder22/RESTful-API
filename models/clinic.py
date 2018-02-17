"""
This is the file for out clinic model.

Clinic:

"""
import sqlite3
from db import db


class ClinicModel(db.Model):
    """Docstring for ClinicModel.

    Clinic:

    """

    __tablename__ = 'clinics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    patients = db.relationship('PatientModel', lazy='dynamic')

    def __init__(self, name):
        """Initialize the class."""
        self.name = name

    def json(self):
        """Return json representation of our object."""
        allpatients = [patient.json() for patient in self.patients.all()]
        return {'name': self.name,
                'patients': allpatients}

    @classmethod
    def findClinic(cls, name):
        """Define method on the resource i.e get."""
        return cls.query.filter_by(name=name).first()

    def insertClinic(self):
        """Insert  and update the database."""
        db.session.add(self)
        db.session.commit()

    def deleteClinic(self):
        """Will delete patient."""
        db.session.delete(self)
        db.session.commit()
