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

@crud_views.route('/edit')
def edit():
    return render_template('edit.html')

@crud_views.route('/delete')
def delete():
    return render_template('index.html')
