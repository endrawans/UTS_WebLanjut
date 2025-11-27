from app import db
from models.mahasiswa import Mahasiswa

def get_all():
    return [m.to_json() for m in Mahasiswa.query.all()]

def get_by_id(id):
    m = Mahasiswa.query.get(id)
    return m.to_json() if m else None

def create(data):
    m = Mahasiswa(
        nim=data["nim"],
        nama=data["nama"],
        alamat=data.get("alamat", "")
    )
    db.session.add(m)
    db.session.commit()
    return m.to_json()

def update(id, data):
    m = Mahasiswa.query.get(id)
    if not m:
        return None
    m.nim = data.get("nim", m.nim)
    m.nama = data.get("nama", m.nama)
    m.alamat = data.get("alamat", m.alamat)
    db.session.commit()
    return m.to_json()

def delete(id):
    m = Mahasiswa.query.get(id)
    if not m:
        return False
    db.session.delete(m)
    db.session.commit()
    return True
