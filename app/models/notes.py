# app/models/notes.py
from app import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    note = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Note {self.name}>"
