from colorama import Fore, Style
from contacts import parse_input, add_contact, get_contacts


def main():
    contacts = {}
    print(Fore.GREEN + "Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.BLUE + "Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.GREEN + "Good bye!")
            break
        elif command == "hello":
            print(Fore.GREEN + "Hi! How can I help you?")
        elif command == "add" or command == "change":
            print(Fore.GREEN + add_contact(args, contacts))
        elif command == "all":
            for name, phone in get_contacts(contacts):
                print(f"{name}: {phone}")
        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()