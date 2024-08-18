from note import Note
def create_account(title, description) -> Note:
    note = Note()
    note.title = title
    note.description = description

    note.save()

    return note