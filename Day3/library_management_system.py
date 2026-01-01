class LibraryItem:
    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name
        self.status = "Available"

    def check_out(self):
        if self.status == "Checked Out":
            print("Item already checked out.")
        else:
            self.status = "Checked Out"
            print("Item checked out successfully.")

    def return_item(self):
        if self.status == "Available":
            print("Item is already available.")
        else:
            self.status = "Available"
            print("Item returned successfully.")

    def display(self):
        print("ID:", self.item_id, "| Name:", self.name, "| Status:", self.status)


items = [
    LibraryItem(1, "Python Book"),
    LibraryItem(2, "Tech Magazine"),
    LibraryItem(3, "Learning DVD")
]

while True:
    print("\n1. Check Out Item")
    print("2. Return Item")
    print("3. Display Items")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_id = int(input("Enter Item ID to check out: "))
        found = False
        for item in items:
            if item.item_id == item_id:
                item.check_out()
                found = True
                break
        if not found:
            print("Invalid Item ID.")

    elif choice == 2:
        item_id = int(input("Enter Item ID to return: "))
        found = False
        for item in items:
            if item.item_id == item_id:
                item.return_item()
                found = True
                break
        if not found:
            print("Invalid Item ID.")

    elif choice == 3:
        print("\nLibrary Items:")
        for item in items:
            item.display()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Enter 1, 2, 3 or 4.")
