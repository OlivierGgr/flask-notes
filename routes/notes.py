from data_access.notes.main import insert_note, get_notes, get_note, delete_note, put_note
from data_access.notes.note_schema import NoteUpdate
from flask import Blueprint, request

note_bp = Blueprint("note", __name__)

@note_bp.route("/notes", methods=["POST"])
def create_note():
    content = request.json.get("content")
    return insert_note(content)

@note_bp.route("/notes", methods=["GET"])
def read_notes():
    return get_notes() 

@note_bp.route("/note/<id>", methods=["GET"])
def read_note(id):
    return get_note(id)

@note_bp.route("/note/<id>", methods=["DELETE"])
def erase_note(id):
    return delete_note(id)

@note_bp.route("/note/<id>", methods=["PUT"])
def update_note(id):
    updated_content_raw = request.json
    updated_content = NoteUpdate(**updated_content_raw)
    updated_content_filtered = updated_content.model_dump(exclude_none=True)
    return put_note(id, updated_content_filtered)