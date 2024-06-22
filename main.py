class Book:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} -- {self.quantity}"

class Student:
    def __init__(self, name: str, dept: str):
        self.name = name
        self.dept = dept
        self.book_allotted = 0

    def __str__(self):
        return f"Name: {self.name}, Department: {self.dept}, Books Allotted: {self.book_allotted}"

    def allot_book(self):
        self.book_allotted += 1

    def deallot_book(self):
        self.book_allotted -= 1

class Library:
    def __init__(self):
        self.books = {}
        self.students = {}

    def add_book(self, book_name: str, qty: int):
        if book_name in self.books:
            self.books[book_name].quantity += qty
        else:
            self.books[book_name] = Book(book_name, qty)

    def delete_book(self, book_name: str, qty: int):
        if book_name not in self.books:
            print("Book is not present")
        else:
            if self.books[book_name].quantity < qty:
                print("Sufficient amount of book is not present")
            else:
                self.books[book_name].quantity -= qty
                if self.books[book_name].quantity == 0:
                    del self.books[book_name]

    def display_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books.values():
                print(book)

    def allot_book(self, student_name: str, student_dept: str, book_name: str):
        if book_name not in self.books or self.books[book_name].quantity <= 0:
            print("Book is not available")
            return

        if student_name not in self.students:
            self.students[student_name] = Student(student_name, student_dept)

        self.books[book_name].quantity -= 1
        self.students[student_name].allot_book()
        print(f"Allotted '{book_name}' to {student_name}")

    def deallot_book(self, student_name: str, book_name: str):
        if student_name not in self.students:
            print("Student not found")
            return

        if self.students[student_name].book_allotted <= 0:
            print("No books to return for this student")
            return

        self.books[book_name].quantity += 1
        self.students[student_name].deallot_book()
        print(f"Returned '{book_name}' from {student_name}")

    def display_students(self):
        if not self.students:
            print("No students found")
        else:
            for student in self.students.values():
                print(student)

if __name__ == '__main__':
    library = Library()
    flag = True

    while flag:
        options = {
            '1': "Add",
            '2': "Delete",
            '3': 'Display Books',
            '4': 'Allot Book',
            '5': 'Deallot Book',
            '6': 'Display Students',
            '7': 'Exit',
        }

        for key, value in options.items():
            print(f"Enter {key} for {value}")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_name = input("Enter the name of the book: ")
            quantity = int(input("Enter the quantity of the book: "))
            library.add_book(book_name, quantity)
        elif choice == '2':
            book_name = input("Enter the name of the book: ")
            quantity = int(input("Enter the quantity of the book to delete: "))
            library.delete_book(book_name, quantity)
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            student_name = input("Enter the name of the student: ")
            student_dept = input("Enter the department of the student: ")
            book_name = input("Enter the name of the book: ")
            library.allot_book(student_name, student_dept, book_name)
        elif choice == '5':
            student_name = input("Enter the name of the student: ")
            book_name = input("Enter the name of the book: ")
            library.deallot_book(student_name, book_name)
        elif choice == '6':
            library.display_students()
        elif choice == '7':
            flag = False
        else:
            print("Enter a valid choice")
