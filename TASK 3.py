import hashlib
import getpass

# File path for the password file
PASSWORD_FILE = "passwd.txt"

def encrypt_password(password):
    # Use SHA-256 for password encryption
    return hashlib.sha256(password.encode()).hexdigest()

def read_password_file():
    with open(PASSWORD_FILE, 'r') as file:
        return [line.strip() for line in file]

def write_password_file(entries):
    with open(PASSWORD_FILE, 'w') as file:
        file.write('\n'.join(entries))

def adduser():
    username = input("Enter the new username: ").lower()
    real_name = input("Enter the real name: ")
    password = getpass.getpass("Enter the password: ")

    # Check if the username already exists
    entries = read_password_file()
    for entry in entries:
        if entry.startswith(username + ":"):
            print("Error: Username already exists.")
            return

    # Add new user entry to the file
    encrypted_password = encrypt_password(password)
    new_entry = f"{username}:{real_name}:{encrypted_password}"
    entries.append(new_entry)

    write_password_file(entries)
    print("User added successfully.")

def deluser():
    username = input("Enter the username to delete: ").lower()

    # Remove user entry from the file
    entries = read_password_file()
    updated_entries = [entry for entry in entries if not entry.startswith(username + ":")]

    if len(updated_entries) == len(entries):
        print("No such user found.")
    else:
        write_password_file(updated_entries)
        print("User deleted successfully.")

def passwd():
    username = input("Enter the username: ").lower()
    current_password = getpass.getpass("Enter the current password: ")

    # Check if the username and current password match
    entries = read_password_file()
    for entry in entries:
        if entry.startswith(username + ":"):
            _, _, stored_password = entry.split(":")
            if encrypt_password(current_password) == stored_password:
                new_password = getpass.getpass("Enter the new password: ")
                verify_new_password = getpass.getpass("Re-enter the new password: ")

                # Check if the new passwords match
                if new_password == verify_new_password:
                    # Update the password in the file
                    entry = f"{username}:{entry.split(':')[1]}:{encrypt_password(new_password)}"
                    entries[entries.index(entry)] = entry
                    write_password_file(entries)
                    print("Password changed successfully.")
                else:
                    print("Error: New passwords do not match.")
                return
            else:
                print("Error: Incorrect current password.")
                return

    print("Error: Username not found.")

def login():
    username = input("Enter the username: ").lower()
    password = getpass.getpass("Enter the password: ")

    # Check if the username and password match
    entries = read_password_file()
    for entry in entries:
        if entry.startswith(username + ":"):
            _, _, stored_password = entry.split(":")
            if encrypt_password(password) == stored_password:
                print("Login successful.")
                return

    print("Login failed.")

def main():
    while True:
        print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Quit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            adduser()
        elif choice == '2':
            deluser()
        elif choice == '3':
            passwd()
        elif choice == '4':
            login()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
