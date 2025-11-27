from app import db

class Kelas(db.Model):
    __tablename__ = "kelas"

    id = db.Column(db.Integer, primary_key=True)
    nama_kelas = db.Column(db.String(50), nullable=False)
    dosen_id = db.Column(db.Integer, db.ForeignKey('dosen.id'))

    dosen = db.relationship("Dosen", backref="kelas")

    def to_json(self):
        return {
            "id": self.id,
            "nama_kelas": self.nama_kelas,
            "dosen_id": self.dosen_id,
            "dosen_nama": self.dosen.nama if self.dosen else None
        }
