import mongoengine
def global_init():
    mongoengine.register_connection(alias='core', db='todo_app')