from note import Note

def display_notes():
    print()
    print("NOtes")
    print("==================")
    for note in Note.objects:
        
        print("-: {}: -> {}".format(note.title, note.description))