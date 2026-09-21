def add_contact():
    name = input("name: ")
    phone = input("phone: ")
    with open("contat.txt", "a") as f:
        f.write(f"{name}, {phone}/n")
    print("contact save ho gia boss!")

def view_contacts():
    print("/n---apka contacts---")
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                print(line.strio())
    except:
        print("abi koi contact nhi h! ")

    while True:
        print("/n1. Add contact")
        print("2. view contacts")
        print("3. exit")
        choice = input("choice (1/2/3): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("ok Boss!")
            break
        else:
            print("ghalat choice!")
