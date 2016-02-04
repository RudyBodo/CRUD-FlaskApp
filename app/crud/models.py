from app.core.db import db

class Barang(db.Model):
    __tablename__ = 'barang'

    id = db.Column(db.Integer, primary_key=True)
    nama_barang = db.Column(db.String(50))
    jenis_barang = db.Column(db.String(50))
    jumlah = db.Column(db.Integer)

    def __init__(self, nama_barang, jenis_barang, jumlah):
        self.nama_barang = nama_barang
        self.jenis_barang = jenis_barang
        self.jumlah = jumlah

    def __repr__(self):
        return '<Barang {}>'.format(self.nama_barang)
