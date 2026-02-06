import getpass

fileName = "python\password manager\passwords.txt"

def addPassword():
    site = input("Input site name: ")
    username = input("Input username: ")
    password = getpass.getpass("Input password: ")
    
    with open(fileName, "a") as f:
        f.write(f"{site} | {username} | {password}\n")
    print("Password saved!")

def viewPasswords():
     with open(fileName, "r") as f:
        for line in f:
         print(line.strip())

def deletePasswords():
    siteToDelete = input("Enter site name to delete: ")
    with open(fileName, "r") as f:
        lines = f.readlines()
    with open(fileName, "w") as f:
        found = False
        for line in lines:
            if not line.lower().startswith(siteToDelete.lower()):
                f.write(line)
            else:
                found = True
    if found:
        print(f"Password for {siteToDelete} deleted!")
    else:
        print(f"No password found for {siteToDelete}.")


def searchPassword():
    siteToSearch = input("Enter site name to search: ")
    found = False
    with open(fileName, "r") as f:
        for line in f:
            if line.lower().startswith(siteToSearch.lower()):
                print(line.strip())
                found = True
    if not found:
        print(f"No password found for {siteToSearch}.")

    
        
while True:
    print("\n Menu:")
    print("1. Add a new password")
    print("2. Delete a password")
    print("3. View passwords")
    print("4. Search password")
    print("5. Exit")
    
    option = input("Select an option: ")
    
    if option == "1":
        addPassword()
    elif option == "2":
        deletePasswords()
    elif option == "3":
        viewPasswords()
    elif option == "4":
        searchPassword()
    else:
        break
    