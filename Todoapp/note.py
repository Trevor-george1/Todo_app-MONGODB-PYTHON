import mongoengine

class Note(mongoengine.Document):
    title = mongoengine.StringField(required=True)
    description = mongoengine.StringField()
    is_completed = mongoengine.BooleanField(default=False)

    meta = {
        'db_alias' : 'core',
        'collection' : 'notes'
    }