students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    print("Student added successfully!")

def search_student():
    name = input("Enter student name to search: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Found:", student)
            return
    print("Student not found.")

def class_average():
    if not students:
        print("No students available.")
        return

    total = 0
    for student in students:
        total += student["marks"]

    avg = total / len(students)
    print("Class Average Marks:", avg)

def top_performer():
    if not students:
        print("No students available.")
        return

    top = students[0]
    for student in students:
        if student["marks"] > top["marks"]:
            top = student

    print("Top Performer:", top)

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Class Average")
    print("4. Top Performer")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        class_average()
    elif choice == "4":
        top_performer()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
