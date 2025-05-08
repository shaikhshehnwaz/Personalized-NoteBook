

from flask import g, jsonify, request
from  flask_restful import Resource

from app.auth.decorators import token_required
from app.md.models import Notes
from app import db
from app.md.serde import NotesSchema


class NoteView(Resource):
    @token_required
    def get(self):
        note=Notes.query.filter_by(user_id=g.user_id).all()
        print(note)
        return NotesSchema(many=True).dump(note)
    
    @token_required
    def post(self):
        new=request.get_json()
        print(new)
        new_data=Notes(data=new['data'],user_id=g.user_id) 
        print(new_data)   
        db.session.add(new_data)
        db.session.commit()

        return NotesSchema().dump(new_data)
    

class NoteSingleView(Resource):
    @token_required
    def get(self,note_id):
        note=Notes.query.filter_by(user_id=g.user_id,id=note_id).first()
        print(note)
        return NotesSchema().dump(note)
    

    @token_required
    def put(self,note_id):
        present_note=Notes.query.filter_by(user_id=g.user_id,id=note_id).first()

        note=request.get_json()

        present_note.data=note["data"]
        db.session.commit()
        return NotesSchema().dump(present_note)
        

    
    @token_required
    def delete(self,note_id):
        present_note=Notes.query.filter_by(user_id=g.user_id,id=note_id).first()
        db.session.delete(present_note)
        db.session.commit()
        return jsonify({"message":"note deleted"})
           