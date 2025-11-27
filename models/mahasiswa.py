from app import db

class Mahasiswa(db.Model):
    __tablename__ = "mahasiswa"

    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200))

    def to_json(self):
        return {
            "id": self.id,
            "nim": self.nim,
            "nama": self.nama,
            "alamat": self.alamat
        }
