from contact_manager import (
    add_contact,
    change_contact,
    get_contact,
    get_all_contacts,
)

COMMAND_CLOSE = {"close", "exit"}
COMMAND_HELLO = {"hello"}
COMMAND_ALL = {"all"}
COMMAND_ADD = {"add"}
COMMAND_CHANGE = {"change"}
COMMAND_PHONE = {"phone"}


def parse_input(user_input: str) -> tuple:
    try:
        cmd, *args = user_input.strip().lower().split(maxsplit=1)
        return cmd, args[0].split() if args else []
    except ValueError:
        return "", []


def handle_command(command: str, args: list, contacts: dict) -> None:
    if command in COMMAND_CLOSE:
        print("Goodbye!")
    elif command in COMMAND_HELLO:
        print("How can I help you?")
    elif command in COMMAND_ALL:
        print(get_all_contacts(contacts))
    elif command in COMMAND_ADD:
        print(add_contact(args, contacts))
    elif command in COMMAND_CHANGE:
        print(change_contact(args, contacts))
    elif command in COMMAND_PHONE:
        print(get_contact(args, contacts))
    else:
        print("Invalid command.")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        handle_command(command, args, contacts)
        if command in COMMAND_CLOSE:
            break


if __name__ == "__main__":
    main()
