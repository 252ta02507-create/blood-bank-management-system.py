# Blood Bank Management System

donors = []
blood_stock = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "AB+": 0,
    "AB-": 0,
    "O+": 0,
    "O-": 0
}


def add_donor():
    print("\n--- Add Blood Donor ---")

    name = input("Enter donor name: ")
    age = int(input("Enter donor age: "))
    blood_group = input("Enter blood group: ").upper()

    if blood_group not in blood_stock:
        print("Invalid blood group.")
        return

    if age < 18:
        print("Donor must be 18 or older.")
        return

    donor = {
        "name": name,
        "age": age,
        "blood_group": blood_group
    }

    donors.append(donor)
    blood_stock[blood_group] += 1

    print("Donor added successfully!")


def view_donors():
    if not donors:
        print("\nNo donor records found.")
        return

    print("\n--- Donor List ---")

    for donor in donors:
        print("Name       :", donor["name"])
        print("Age        :", donor["age"])
        print("Blood Group:", donor["blood_group"])
        print("------------------------")


def view_stock():
    print("\n--- Blood Stock ---")

    for blood_group, quantity in blood_stock.items():
        print(f"{blood_group}: {quantity} unit(s)")


def search_blood():
    blood_group = input("Enter required blood group: ").upper()

    if blood_group not in blood_stock:
        print("Invalid blood group.")
        return

    quantity = blood_stock[blood_group]

    if quantity > 0:
        print(f"{quantity} unit(s) of {blood_group} blood available.")
    else:
        print(f"{blood_group} blood is currently unavailable.")


def issue_blood():
    blood_group = input("Enter blood group to issue: ").upper()

    if blood_group not in blood_stock:
        print("Invalid blood group.")
        return

    if blood_stock[blood_group] > 0:
        blood_stock[blood_group] -= 1
        print(f"1 unit of {blood_group} blood issued successfully.")
    else:
        print("Blood stock is not available.")


while True:

    print("\n================================")
    print("   BLOOD BANK MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Donor")
    print("2. View Donors")
    print("3. View Blood Stock")
    print("4. Search Blood")
    print("5. Issue Blood")
    print("6. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_donor()

    elif choice == "2":
        view_donors()

    elif choice == "3":
        view_stock()

    elif choice == "4":
        search_blood()

    elif choice == "5":
        issue_blood()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
