from db import db

class Dosen(db.Model):
    __tablename__ = "dosen"

    id = db.Column(db.Integer, primary_key=True)
    nidn = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    prodi = db.Column(db.String(100))

    def to_json(self):
        return {
            "id": self.id,
            "nidn": self.nidn,
            "nama": self.nama,
            "prodi": self.prodi
        }
