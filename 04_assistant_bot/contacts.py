def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): 
    name, phone = args
    contacts[name] = phone
    return "Contact added/modified"

def get_contacts(contacts):
    for name, phone in contacts.items():
        yield name, phone