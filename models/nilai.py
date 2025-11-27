from db import db

class Nilai(db.Model):
    __tablename__ = "nilai"

    id = db.Column(db.Integer, primary_key=True)
    mahasiswa_id = db.Column(db.Integer, db.ForeignKey('mahasiswa.id'))
    matakuliah_id = db.Column(db.Integer, db.ForeignKey('matakuliah.id'))
    nilai = db.Column(db.Float)

    mahasiswa = db.relationship("Mahasiswa", backref="nilai")
    matakuliah = db.relationship("MataKuliah", backref="nilai")

    def to_json(self):
        return {
            "id": self.id,
            "mahasiswa_id": self.mahasiswa_id,
            "matakuliah_id": self.matakuliah_id,
            "nilai": self.nilai,
            "mahasiswa_nama": self.mahasiswa.nama if self.mahasiswa else None,
            "matakuliah_nama": self.matakuliah.nama if self.matakuliah else None
        }
