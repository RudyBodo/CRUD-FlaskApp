from flask import Blueprint, render_template, request, session, abort, redirect
from app.core.db import db
from models import Barang

crud_views = Blueprint('crud',__name__,
                static_folder ='../../static',
                template_folder ='../../templates')

#view all stock
@crud_views.route('/')
def home():
    goods = Barang.query.all()
    return render_template('index.html', **locals())

@crud_views.route('/detail/<int:id>')
def view(id):
    barang = Barang.query.get(id)
    return render_template('detail.html', **locals())

#add Stock in store
@crud_views.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        namaBarang = request.form.get("NamaBarang", None)
        jenisBarang = request.form.get("JenisBarang", None)
        value = request.form.get("Jumlah", None)
        iNput = Barang(namaBarang,jenisBarang,value)
        db.session.add(iNput)
        db.session.commit()
        return redirect('/')

    return render_template('add.html',**locals())

@crud_views.route('/edit/<int:id>', methods=["POST", "GET"])
def edit(id):
    barang = Barang.query.get(id)
    if request.method == "POST":
        newBarang = request.form.get("NamaBarang", None)
        newJenisBarang = request.form.get("JenisBarang", None)
        newValue = request.form.get("Jumlah", None)
        barang.nama_barang = newBarang
        barang.jenis_barang = newJenisBarang
        barang.jumlah = newValue
        newData = Barang(newBarang, newJenisBarang, newValue)
        db.session.add(newData)
        db.session.commit()
        return redirect('/')

    return render_template('edit.html', **locals())

@crud_views.route('/delete/<int:id>')
def delete(id):
    barang = Barang.query.get(id)
    db.session.delete(barang)
    db.session.commit()
    return redirect('/')
