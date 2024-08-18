import services.create_account as svc
def fetch_data_to_create_note():
    title = input("Enter the title of note: ").rstrip().lower()
    description = input("Description: ")

    #print("1. {}: {}".format(title, description))
    note = svc.create_account(title, description)
    return note

    