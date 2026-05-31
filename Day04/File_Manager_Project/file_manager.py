from pathlib import Path

# ==========================================================
# File Manager Project
# ==========================================================
#
# Features:
# 1. Create File
# 2. Read File
# 3. Update File
#    - Rename File
#    - Overwrite Data
#    - Append Data
# 4. Delete File
# 5. Exit
#
# ==========================================================


# ==========================================================
# Display All Files and Folders
# ==========================================================

def readFileAndFolder():

    path = Path(".")

    print("\n===== FILES & FOLDERS =====")

    count = 1

    for item in path.iterdir():

        # Ignore hidden files/folders
        if not item.name.startswith("."):

            print(f"{count} : {item}")

            count += 1

    print()


# ==========================================================
# Create File
# ==========================================================

def createFile():

    try:

        readFileAndFolder()

        name = input("Enter file name: ")

        p = Path(name)

        if not p.exists():

            with open(p, "w") as fs:

                data = input("Enter file content: ")

                fs.write(data)

            print("✅ File created successfully.")

        else:

            print("❌ File already exists.")

    except Exception as err:

        print(f"Error: {err}")


# ==========================================================
# Read File
# ==========================================================

def readFile():

    try:

        readFileAndFolder()

        name = input("Which file do you want to read? ")

        p = Path(name)

        if p.exists() and p.is_file():

            with open(p, "r") as fs:

                data = fs.read()

                print("\n===== FILE CONTENT =====")
                print(data)

            print("\n✅ File read successfully.")

        else:

            print("❌ File does not exist.")

    except Exception as err:

        print(f"Error: {err}")


# ==========================================================
# Update File
# ==========================================================

def updateFile():

    try:

        readFileAndFolder()

        name = input("Which file do you want to update? ")

        p = Path(name)

        if p.exists() and p.is_file():

            print("\n1. Rename File")
            print("2. Overwrite File Content")
            print("3. Append File Content")

            choice = int(input("Enter your choice: "))

            # Rename File

            if choice == 1:

                new_name = input("Enter new file name: ")

                p2 = Path(new_name)

                if p2.exists():

                    print("❌ File already exists.")

                else:

                    p.rename(p2)

                    print("✅ File renamed successfully.")

            # Overwrite Content

            elif choice == 2:

                with open(p, "w") as fs:

                    data = input(
                        "Enter new content (old content will be removed): "
                    )

                    fs.write(data)

                print("✅ File updated successfully.")

            # Append Content

            elif choice == 3:

                with open(p, "a") as fs:

                    data = input(
                        "Enter content to append: "
                    )

                    fs.write(data)

                print("✅ Data appended successfully.")

            else:

                print("❌ Invalid choice.")

        else:

            print("❌ File does not exist.")

    except Exception as err:

        print(f"Error: {err}")


# ==========================================================
# Delete File
# ==========================================================

def deleteFile():

    try:

        readFileAndFolder()

        name = input("Which file do you want to delete? ")

        p = Path(name)

        if p.exists() and p.is_file():

            p.unlink()

            print("✅ File deleted successfully.")

        else:

            print("❌ File does not exist.")

    except Exception as err:

        print(f"Error: {err}")


# ==========================================================
# Main Menu
# ==========================================================

while True:

    print("\n===================================")
    print("         FILE MANAGER")
    print("===================================")

    print("1. Create File")
    print("2. Read File")
    print("3. Update File")
    print("4. Delete File")
    print("5. Exit")

    try:

        check = int(input("Enter your choice: "))

        if check == 1:

            createFile()

        elif check == 2:

            readFile()

        elif check == 3:

            updateFile()

        elif check == 4:

            deleteFile()

        elif check == 5:

            print("👋 Thank you for using File Manager.")
            break

        else:

            print("❌ Invalid Choice.")

    except ValueError:

        print("❌ Please enter a valid number.")