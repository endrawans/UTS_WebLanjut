from app import db

class MataKuliah(db.Model):
    __tablename__ = "matakuliah"

    id = db.Column(db.Integer, primary_key=True)
    kode = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    sks = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "kode": self.kode,
            "nama": self.nama,
            "sks": self.sks
        }
