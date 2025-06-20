# File Management Application

import os

# Create a file
def file_create(filename):
    try:
        with open(filename, "x") as file:
            print(f"File '{filename}' created successfully!")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# View all files in the directory
def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found!")
    else:
        print("Files in the directory:")
        for file in files:
            print(file)

# Delete a file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' has been deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An exception occurred: {e}")

# Read a file
def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An exception occurred: {e}")

# Edit (append to) a file
def edit_file(filename):
    try:
        with open(filename, "a") as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print(f"Content added to '{filename}' successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An exception occurred: {e}")

# Main function to interact with the user
def main():
    while True:
        print('\nFILE MANAGEMENT APP')
        print('1: Create file')
        print('2: View all files')
        print('3: Delete file')
        print('4: Read file')
        print('5: Edit file')
        print('6: Exit')

        choice = input('Enter your choice (1–6):').strip()

        if choice == '1':
            filename = input("Enter the file name to create: ")
            file_create(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the file name to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the file name to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the file name to edit: ")
            edit_file(filename)
        elif choice == '6':
            print("Closing the app.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
