from flask import current_app, jsonify
from sqlalchemy import func

from db.models.note import Note
from extensions import db
import logging

def insert_note(content):
    with current_app.app_context():
        try:
            new_note = Note(
                content=content
            )
            db.session.add(new_note)
            db.session.commit()
            print(f"Note créée avec ID: { new_note.id }")
            return jsonify({ "id": new_note.id }), 201
        except Exception as error:
            return jsonify({"error": str(error)}), 500
    
def get_notes():
    with current_app.app_context():
        try:
            notes = db.session.execute(
                db.select(Note)
            ).scalars().all()

            notes_as_dict = [Note.to_dict(note) for note in notes]
            return jsonify(notes_as_dict), 200
        except Exception as error:
            logging.exception("Erreur lors de la récupération des notes")
            return jsonify({"error": str(error)}), 500
        
def get_note(id):
    with current_app.app_context():
        try:
            note = db.session.execute(
                db.select(Note).where(Note.id == id)
            ).scalar_one()

            note_as_dict = Note.to_dict(note)
            return jsonify(note_as_dict), 200
        except Exception as error:
            logging.exception("Erreur lors de la récupération d'une note")
            return jsonify({"error": str(error)}), 500
        
def delete_note(id):
    with current_app.app_context():
        try:
            db.session.execute(
                db.delete(Note).where(Note.id == id)
            )
            db.session.commit()
            return "Note deleted", 200
        except Exception as error:
            logging.exception("Erreur lors de la suppression de la note" + id)
            return jsonify({"error": str(error)}), 500

def put_note(id, updated_content):
    with current_app.app_context():
        try:
            updated_content["updated_at"] = func.now()

            update_statement = db.update(Note).where(Note.id == id).values(updated_content)
            db.session.execute(update_statement)
            db.session.commit()
            return jsonify({ "id": id }), 200
        except Exception as error:
            logging.exception("Erreur lors de la suppression de la note" + id)
            return jsonify({"error": str(error)}), 500