from . import db

class Student(db.Model):
    __tablename__ = 'studenti'
    
    idstudent = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100))
    prenume = db.Column(db.String(100))
    specializare = db.Column(db.String(100))
    varsta = db.Column(db.Integer)

    # Relația cu Cursuri, cu ștergerea automată a cursurilor asociate
    cursuri = db.relationship('Curs', backref='student_asociat', cascade="all, delete", passive_deletes=True)

class Profesor(db.Model):
    __tablename__ = 'profesori'
    
    idprofesor = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100))
    prenume = db.Column(db.String(100))
    adresa = db.Column(db.String(255))

    # Relație cu Cursuri, cu ștergerea automată a cursurilor asociate
    cursuri = db.relationship('Curs', backref='profesor_asociat', cascade="all, delete", passive_deletes=True)

class Curs(db.Model):
    __tablename__ = 'cursuri'

    idcurs = db.Column(db.Integer, primary_key=True)
    numecurs = db.Column(db.String(100))
    ora = db.Column(db.String(10))
    sala = db.Column(db.String(50))

    # Relație cu Student, cu ștergerea automată a cursurilor când studentul este șters
    idstudent = db.Column(db.Integer, db.ForeignKey('studenti.idstudent', ondelete='CASCADE'), nullable=True)
    idprofesor = db.Column(db.Integer, db.ForeignKey('profesori.idprofesor', ondelete='CASCADE'), nullable=True)

    student = db.relationship('Student', backref=db.backref('student_asociat', passive_deletes=True))
    profesor = db.relationship('Profesor', backref=db.backref('profesor_asociat', passive_deletes=True))
