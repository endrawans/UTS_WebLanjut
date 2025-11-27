from app import db
from models.dosen import Dosen

def get_all():
    return [d.to_json() for d in Dosen.query.all()]

def get_by_id(id):
    d = Dosen.query.get(id)
    return d.to_json() if d else None

def create(data):
    d = Dosen(
        nidn=data["nidn"],
        nama=data["nama"],
        prodi=data.get("prodi", "")
    )
    db.session.add(d)
    db.session.commit()
    return d.to_json()

def update(id, data):
    d = Dosen.query.get(id)
    if not d:
        return None
    d.nidn = data.get("nidn", d.nidn)
    d.nama = data.get("nama", d.nama)
    d.prodi = data.get("prodi", d.prodi)
    db.session.commit()
    return d.to_json()

def delete(id):
    d = Dosen.query.get(id)
    if not d:
        return False
    db.session.delete(d)
    db.session.commit()
    return True
