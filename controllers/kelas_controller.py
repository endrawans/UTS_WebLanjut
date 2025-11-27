from db import db
from models.kelas import Kelas

def get_all():
    return [k.to_json() for k in Kelas.query.all()]

def get_by_id(id):
    k = Kelas.query.get(id)
    return k.to_json() if k else None

def create(data):
    k = Kelas(
        nama_kelas=data["nama_kelas"],
        dosen_id=data.get("dosen_id")
    )
    db.session.add(k)
    db.session.commit()
    return k.to_json()

def update(id, data):
    k = Kelas.query.get(id)
    if not k:
        return None
    k.nama_kelas = data.get("nama_kelas", k.nama_kelas)
    k.dosen_id = data.get("dosen_id", k.dosen_id)
    db.session.commit()
    return k.to_json()

def delete(id):
    k = Kelas.query.get(id)
    if not k:
        return False
    db.session.delete(k)
    db.session.commit()
    return True
