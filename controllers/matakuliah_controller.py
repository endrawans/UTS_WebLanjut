from app import db
from models.matakuliah import MataKuliah

def get_all():
    return [mk.to_json() for mk in MataKuliah.query.all()]

def get_by_id(id):
    mk = MataKuliah.query.get(id)
    return mk.to_json() if mk else None

def create(data):
    mk = MataKuliah(
        kode=data["kode"],
        nama=data["nama"],
        sks=data["sks"]
    )
    db.session.add(mk)
    db.session.commit()
    return mk.to_json()

def update(id, data):
    mk = MataKuliah.query.get(id)
    if not mk:
        return None
    mk.kode = data.get("kode", mk.kode)
    mk.nama = data.get("nama", mk.nama)
    mk.sks = data.get("sks", mk.sks)
    db.session.commit()
    return mk.to_json()

def delete(id):
    mk = MataKuliah.query.get(id)
    if not mk:
        return False
    db.session.delete(mk)
    db.session.commit()
    return True
