from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Student, Profesor, Curs

# Definire Blueprint
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('base.html')

# CRUD pentru Studenți
@routes.route('/studenti', methods=['GET', 'POST'])
def studenti():
    studenti = Student.query.all()
    return render_template('studenti.html', studenti=studenti)

@routes.route('/adaugare_student', methods=['POST'])
def adaugare_student():
    if request.method == 'POST':
        nume = request.form['nume']
        prenume = request.form['prenume']
        specializare = request.form['specializare']
        varsta = request.form['varsta']

        student = Student(nume=nume, prenume=prenume, specializare=specializare, varsta=int(varsta))
        db.session.add(student)
        db.session.commit()
        flash('Student adăugat cu succes!', 'success')
        return redirect(url_for('routes.studenti'))  # Prefix "routes" pentru Blueprint

@routes.route('/stergere_student/<int:id>', methods=['GET', 'POST'])
def stergere_student(id):
    student = Student.query.get_or_404(id)
    
    # Șterge cursurile asociate studentului înainte de a-l șterge
    for curs in student.cursuri:
        db.session.delete(curs)
    
    db.session.delete(student)
    db.session.commit()
    flash('Student și cursurile asociate au fost șterse cu succes!', 'success')
    return redirect(url_for('routes.studenti'))  # Prefix "routes" pentru Blueprint


@routes.route('/editare_student/<int:id>', methods=['GET', 'POST'])
def editare_student(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.nume = request.form['nume']
        student.prenume = request.form['prenume']
        student.specializare = request.form['specializare']
        student.varsta = request.form['varsta']

        db.session.commit()
        flash('Student actualizat cu succes!', 'success')
        return redirect(url_for('routes.studenti'))

    return render_template('editare_student.html', student=student)

@routes.route('/actualizeaza_student/<int:id>', methods=['POST'])
def actualizeaza_student(id):
    student = Student.query.get_or_404(id)

    student.nume = request.form['nume']
    student.prenume = request.form['prenume']
    student.specializare = request.form['specializare']
    student.varsta = request.form['varsta']

    db.session.commit()
    flash('Student actualizat cu succes!', 'success')
    return redirect(url_for('routes.studenti'))  # Redirect către pagina de studenți




# CRUD pentru Profesori
@routes.route('/profesori', methods=['GET', 'POST'])
def profesori():
    profesori = Profesor.query.all()
    return render_template('profesori.html', profesori=profesori)

@routes.route('/adaugare_profesor', methods=['POST'])
def adaugare_profesor():
    if request.method == 'POST':
        nume = request.form['nume']
        prenume = request.form['prenume']
        adresa = request.form['adresa']

        profesor = Profesor(nume=nume, prenume=prenume, adresa=adresa)
        db.session.add(profesor)
        db.session.commit()
        flash('Profesor adăugat cu succes!', 'success')
        return redirect(url_for('routes.profesori'))  # Prefix "routes" pentru Blueprint

@routes.route('/stergere_profesor/<int:id>', methods=['GET', 'POST'])
def stergere_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    db.session.delete(profesor)
    db.session.commit()
    flash('Profesor șters cu succes!', 'success')
    return redirect(url_for('routes.profesori'))  # Prefix "routes" pentru Blueprint

@routes.route('/editare_profesor/<int:id>', methods=['GET', 'POST'])
def editare_profesor(id):
    profesor = Profesor.query.get_or_404(id)

    if request.method == 'POST':
        profesor.nume = request.form['nume']
        profesor.prenume = request.form['prenume']
        profesor.adresa = request.form['adresa']

        db.session.commit()
        flash('Profesor actualizat cu succes!', 'success')
        return redirect(url_for('routes.profesori'))  # Redirect către lista profesorilor

    return render_template('editare_profesor.html', profesor=profesor)

@routes.route('/actualizeaza_profesor/<int:id>', methods=['POST'])
def actualizeaza_profesor(id):
    profesor = Profesor.query.get_or_404(id)

    profesor.nume = request.form['nume']
    profesor.prenume = request.form['prenume']
    profesor.adresa = request.form['adresa']

    db.session.commit()
    flash('Profesor actualizat cu succes!', 'success')
    return redirect(url_for('routes.profesori'))  # Redirect către lista profesorilor


# CRUD pentru Cursuri
@routes.route('/cursuri', methods=['GET', 'POST'])
def cursuri():
    cursuri = Curs.query.all()  # Preia toate cursurile
    studenti = Student.query.all()  # Preia toți studenții
    profesori = Profesor.query.all()  # Preia toți profesorii
    return render_template('cursuri.html', cursuri=cursuri, studenti=studenti, profesori=profesori)

@routes.route('/adaugare_curs', methods=['POST'])
def adaugare_curs():
    if request.method == 'POST':
        numecurs = request.form['numecurs']
        idstudent = request.form['idstudent']
        idprofesor = request.form['idprofesor']
        ora = request.form['ora']
        sala = request.form['sala']

        curs = Curs(numecurs=numecurs, idstudent=idstudent, idprofesor=idprofesor, ora=ora, sala=sala)
        db.session.add(curs)
        db.session.commit()
        flash('Curs adăugat cu succes!', 'success')
        return redirect(url_for('routes.cursuri'))  # Prefix "routes" pentru Blueprint

@routes.route('/stergere_curs/<int:id>', methods=['GET', 'POST'])
def stergere_curs(id):
    curs = Curs.query.get_or_404(id)
    db.session.delete(curs)
    db.session.commit()
    flash('Curs șters cu succes!', 'success')
    return redirect(url_for('routes.cursuri'))  # Prefix "routes" pentru Blueprint

@routes.route('/editare_curs/<int:id>', methods=['GET', 'POST'])
def editare_curs(id):
    curs = Curs.query.get_or_404(id)

    if request.method == 'POST':
        curs.numecurs = request.form['numecurs']
        curs.ora = request.form['ora']
        curs.sala = request.form['sala']
        curs.idstudent = request.form['idstudent']
        curs.idprofesor = request.form['idprofesor']

        db.session.commit()
        flash('Curs actualizat cu succes!', 'success')
        return redirect(url_for('routes.cursuri'))  # Redirect către pagina de cursuri

    # Obține lista de studenți și profesori pentru dropdown
    studenti = Student.query.all()
    profesori = Profesor.query.all()

    return render_template('editare_curs.html', curs=curs, studenti=studenti, profesori=profesori)

@routes.route('/actualizeaza_curs/<int:id>', methods=['POST'])
def actualizeaza_curs(id):
    curs = Curs.query.get_or_404(id)

    curs.numecurs = request.form['numecurs']
    curs.ora = request.form['ora']
    curs.sala = request.form['sala']
    curs.idstudent = request.form['idstudent']
    curs.idprofesor = request.form['idprofesor']

    db.session.commit()
    flash('Curs actualizat cu succes!', 'success')
    return redirect(url_for('routes.cursuri'))  # Redirect către pagina de cursuri


