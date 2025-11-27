from db import db
from models.nilai import Nilai

def get_all():
    return [n.to_json() for n in Nilai.query.all()]

def get_by_id(id):
    n = Nilai.query.get(id)
    return n.to_json() if n else None

def create(data):
    n = Nilai(
        mahasiswa_id=data["mahasiswa_id"],
        matakuliah_id=data["matakuliah_id"],
        nilai=data["nilai"]
    )
    db.session.add(n)
    db.session.commit()
    return n.to_json()

def update(id, data):
    n = Nilai.query.get(id)
    if not n:
        return None
    n.mahasiswa_id = data.get("mahasiswa_id", n.mahasiswa_id)
    n.matakuliah_id = data.get("matakuliah_id", n.matakuliah_id)
    n.nilai = data.get("nilai", n.nilai)
    db.session.commit()
    return n.to_json()

def delete(id):
    n = Nilai.query.get(id)
    if not n:
        return False
    db.session.delete(n)
    db.session.commit()
    return True
