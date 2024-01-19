from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_title = request.form.get('title')  # Get the title from the form
        note_content = request.form.get('note')
        note_id = request.form.get('note_id')

        if len(note_content) < 1:
            flash('Note is too short!', category='error')
        else:
            if note_id:  # If editing an existing note
                note = Note.query.get(int(note_id))
                if note and note.user_id == current_user.id:
                    note.title = note_title  # Update the title
                    note.data = note_content
                    db.session.commit()
                    flash('Note updated!', category='success')
            else:  # If creating a new note
                new_note = Note(data=note_content, title=note_title, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
