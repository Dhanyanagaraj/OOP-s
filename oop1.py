from datetime import datetime
class Book:
    def __init__(self, isbn, title, author, genre, published_date, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.published_date = published_date
        self.total_copies = total_copies
        self.available_copies = total_copies

    def checkout(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False


class Member:
    def __init__(self, member_id, name, contact_info, address):
        self.member_id = member_id
        self.name = name
        self.contact_info = contact_info
        self.address = address
        self.books_checked_out = []

    def checkout_book(self, book):
        if book.checkout():
            self.books_checked_out.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book.return_book():
            self.books_checked_out.remove(book)
            return True
        else:
            return False


class Librarian:
    def __init__(self, librarian_id, name, contact_info):
        self.librarian_id = librarian_id
        self.name = name
        self.contact_info = contact_info

    def add_book(self, book, library):
        library.add_book(book)

    def remove_book(self, book, library):
        library.remove_book(book)

    def add_member(self, member, library):
        library.add_member(member)

    def remove_member(self, member, library):
        library.remove_member(member)


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.librarians = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def search_books(self, title=None, author=None):
        if title and author:
            return [book for book in self.books if book.title == title and book.author == author]
        elif title:
            return [book for book in self.books if book.title == title]
        elif author:
            return [book for book in self.books if book.author == author]
        else:
            return []

    def list_available_books(self):
        return [book for book in self.books if book.available_copies > 0]

    def list_checked_out_books(self, member):
        return [book for book in member.books_checked_out]

    def list_overdue_books(self):
        # Add logic to determine overdue books based on return dates
        pass

class Transaction:
    def __init__(self, transaction_id, date, transaction_type, member, book):
        self._transaction_id = transaction_id
        self._date = date
        self._transaction_type = transaction_type
        self._member = member
        self._book = book

    def transaction_id(self):
        return self._transaction_id

    def transaction_id(self, value):
        self._transaction_id = value

    def date(self):
        return self._date

    def date(self, value):
        self._date = value

    def transaction_type(self):
        return self._transaction_type

    def transaction_type(self, value):
        self._transaction_type = value

    def member(self):
        return self._member

    def member(self, value):
        self._member = value

    def book(self):
        return self._book

    def book(self, value):
        self._book = value


class Reservation:
    def __init__(self, reservation_id, member, book, status):
        self._reservation_id = reservation_id
        self._member = member
        self._book = book
        self._status = status

    def reservation_id(self):
        return self._reservation_id

    def reservation_id(self, value):
        self._reservation_id = value

    def member(self):
        return self._member
    
    def member(self, value):
        self._member = value

    def book(self):
        return self._book
    
    def book(self, value):
        self._book = value

    def status(self):
        return self._status

    def status(self, value):
        self._status = value


class Fine:
    def __init__(self, fine_id, member, amount, status):
        self._fine_id = fine_id
        self._member = member
        self._amount = amount
        self._status = status

    def fine_id(self):
        return self._fine_id

    def fine_id(self, value):
        self._fine_id = value

    def member(self):
        return self._member

    def member(self, value):
        self._member = value

    def amount(self):
        return self._amount

    def amount(self, value):
        self._amount = value

    def status(self):
        return self._status

    def status(self, value):
        self._status = value


class Author:
    def __init__(self, author_id, name, nationality):
        self._author_id = author_id
        self._name = name
        self._nationality = nationality

    def author_id(self):
        return self._author_id
    
    def author_id(self, value):
        self._author_id = value

    def name(self):
        return self._name

    def name(self, value):
        self._name = value


    def nationality(self):
        return self._nationality

    def nationality(self, value):
        self._nationality = value


class Genre:
    def __init__(self, genre_id, name):
        self._genre_id = genre_id
        self._name = name

    def genre_id(self):
        return self._genre_id

    def genre_id(self, value):
        self._genre_id = value

    def name(self):
        return self._name

    def name(self, value):
        self._name = value


class Publisher:
    def __init__(self, publisher_id, name, location):
        self._publisher_id = publisher_id
        self._name = name
        self._location = location


    def publisher_id(self):
        return self._publisher_id

    def publisher_id(self, value):
        self._publisher_id = value

    def name(self):
        return self._name

    def name(self, value):
        self._name = value

    def location(self):
        return self._location
    
    def location(self, value):
        self._location = value


#Control Entities
class LibraryManager:
    def __init__(self, library):
        self.library = library

    def add_book(self, book):
        self.library.add_book(book)

    def remove_book(self, book):
        self.library.remove_book(book)

    def add_member(self, member):
        self.library.add_member(member)

    def remove_member(self, member):
        self.library.remove_member(member)


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def create_transaction(self, transaction_id, date, transaction_type, member, book):
        transaction = Transaction(transaction_id, date, transaction_type, member, book)
        self.transactions.append(transaction)
        return transaction


class ReservationManager:
    def __init__(self):
        self.reservations = []

    def create_reservation(self, reservation_id, member, book, status):
        reservation = Reservation(reservation_id, member, book, status)
        self.reservations.append(reservation)
        return reservation

    def fulfill_reservation(self, reservation):
        reservation.status = "fulfilled"


class FineManager:
    def __init__(self):
        self.fines = []

    def create_fine(self, fine_id, member, amount, status):
        fine = Fine(fine_id, member, amount, status)
        self.fines.append(fine)
        return fine

    def pay_fine(self, fine):
        fine.status = "paid"


class AuthorManager:
    def __init__(self):
        self.authors = []

    def create_author(self, author_id, name, nationality):
        author = Author(author_id, name, nationality)
        self.authors.append(author)
        return author


class GenreManager:
    def __init__(self):
        self.genres = []

    def create_genre(self, genre_id, name):
        genre = Genre(genre_id, name)
        self.genres.append(genre)
        return genre


class PublisherManager:
    def __init__(self):
        self.publishers = []

    def create_publisher(self, publisher_id, name, location):
        publisher = Publisher(publisher_id, name, location)
        self.publishers.append(publisher)
        return publisher


class MemberManager:
    def __init__(self, library):
        self.library = library

    def register_member(self, member_id, name, contact_info, address):
        member = Member(member_id, name, contact_info, address)
        self.library.add_member(member)
        return member

    def remove_member(self, member):
        self.library.remove_member(member)


class LibrarianManager:
    def __init__(self, library):
        self.library = library

    def hire_librarian(self, librarian_id, name, contact_info):
        librarian = Librarian(librarian_id, name, contact_info)
        self.library.librarians.append(librarian)
        return librarian

    def remove_librarian(self, librarian):
        self.library.librarians.remove(librarian)


class ReportManager:
    def __init__(self, library):
        self.library = library

    def generate_overdue_report(self):
        overdue_books = []
        today = datetime.date.today()

        for member in self.library.members:
            for book in member.books_checked_out:
                if book.return_date < today:
                    overdue_books.append((book, member))

        return overdue_books

    def generate_inventory_report(self):
        inventory_summary = {}

        for book in self.library.books:
            if book.title in inventory_summary:
                inventory_summary[book.title] += book.available_copies
            else:
                inventory_summary[book.title] = book.available_copies

        return inventory_summary


#Boundary entity.
class LibraryConsole:
    def __init__(self, library_manager, transaction_manager, reservation_manager, fine_manager,
                 author_manager, genre_manager, publisher_manager, member_manager, librarian_manager,
                 report_manager):
        self.library_manager = library_manager
        self.transaction_manager = transaction_manager
        self.reservation_manager = reservation_manager
        self.fine_manager = fine_manager
        self.author_manager = author_manager
        self.genre_manager = genre_manager
        self.publisher_manager = publisher_manager
        self.member_manager = member_manager
        self.librarian_manager = librarian_manager
        self.report_manager = report_manager

    def display_menu(self):
        print("===== Library Management System Menu =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Member")
        print("4. Remove Member")
        print("5. Checkout Book")
        print("6. Return Book")
        print("7. Generate Overdue Report")
        print("8. Generate Inventory Report")
        print("9. Exit")
        print("=========================================")

    def get_user_input(self):
        return input("Enter your choice: ")

    def execute_user_option(self, option):
        if option == "1":
            # Add Book
            pass
        elif option == "2":
            # Remove Book
            pass
        elif option == "3":
            # Add Member
            pass
        elif option == "4":
            # Remove Member
            pass
        elif option == "5":
            # Checkout Book
            pass
        elif option == "6":
            # Return Book
            pass
        elif option == "7":
            # Generate Overdue Report
            self.report_manager.generate_overdue_report()
        elif option == "8":
            # Generate Inventory Report
            self.report_manager.generate_inventory_report()
        elif option == "9":
            print("Exiting. Goodbye!")
        else:
            print("Invalid option. Please try again.")

    def display_output(self, message):
        print(message)



class TransactionUI:
    def __init__(self, transaction_manager, member_manager, book_manager):
        self.transaction_manager = transaction_manager
        self.member_manager = member_manager
        self.book_manager = book_manager

    def process_checkout(self):
        member_id = input("Enter Member ID: ")
        book_isbn = input("Enter Book ISBN: ")

        # Retrieve member and book objects
        member = self.member_manager.get_member_by_id(member_id)
        book = self.book_manager.get_book_by_isbn(book_isbn)

        if member is not None and book is not None:
            if self.transaction_manager.create_transaction("checkout", member, book):
                print(f"Book '{book.title}' has been checked out by {member.name}.")
            else:
                print("Unable to process checkout. Please try again.")
        else:
            print("Invalid member ID or book ISBN. Please try again.")

    def process_return(self):
        member_id = input("Enter Member ID: ")
        book_isbn = input("Enter Book ISBN: ")

        # Retrieve member and book objects
        member = self.member_manager.get_member_by_id(member_id)
        book = self.book_manager.get_book_by_isbn(book_isbn)

        if member is not None and book is not None:
            if self.transaction_manager.create_transaction("return", member, book):
                print(f"Book '{book.title}' has been returned by {member.name}.")
            else:
                print("Unable to process return. Please try again.")
        else:
            print("Invalid member ID or book ISBN. Please try again.")


class ReservationUI:
    def __init__(self, reservation_manager, member_manager, book_manager):
        self.reservation_manager = reservation_manager
        self.member_manager = member_manager
        self.book_manager = book_manager

    def make_reservation(self):
        member_id = input("Enter Member ID: ")
        book_isbn = input("Enter Book ISBN: ")

        # Retrieve member and book objects
        member = self.member_manager.get_member_by_id(member_id)
        book = self.book_manager.get_book_by_isbn(book_isbn)

        if member is not None and book is not None:
            reservation = self.reservation_manager.create_reservation(member, book)
            if reservation is not None:
                print(f"Reservation {reservation.reservation_id} created for {book.title}.")
            else:
                print("Unable to make reservation. Please try again.")
        else:
            print("Invalid member ID or book ISBN. Please try again.")

    def fulfill_reservation(self):
        reservation_id = input("Enter Reservation ID: ")
        
        # Retrieve reservation object
        reservation = self.reservation_manager.get_reservation_by_id(reservation_id)

        if reservation is not None and reservation.status == "pending":
            reservation.status = "fulfilled"
            print(f"Reservation {reservation.reservation_id} fulfilled.")
        else:
            print("Invalid reservation ID or reservation already fulfilled.")


class FineUI:
    def __init__(self, fine_manager, member_manager):
        self.fine_manager = fine_manager
        self.member_manager = member_manager

    def create_fine(self):
        member_id = input("Enter Member ID: ")
        amount = float(input("Enter Fine Amount: "))

        # Retrieve member object
        member = self.member_manager.get_member_by_id(member_id)

        if member is not None:
            fine = self.fine_manager.create_fine(member, amount)
            if fine is not None:
                print(f"Fine {fine.fine_id} created for {member.name}.")
            else:
                print("Unable to create fine. Please try again.")
        else:
            print("Invalid member ID. Please try again.")

    def pay_fine(self):
        fine_id = input("Enter Fine ID: ")
        
        # Retrieve fine object
        fine = self.fine_manager.get_fine_by_id(fine_id)

        if fine is not None and fine.status == "unpaid":
            self.fine_manager.pay_fine(fine)
            print(f"Fine {fine.fine_id} paid.")
        else:
            print("Invalid fine ID or fine already paid.")



class AuthorUI:
    def __init__(self, author_manager):
        self.author_manager = author_manager

    def create_author(self):
        name = input("Enter Author Name: ")
        nationality = input("Enter Author Nationality: ")

        # Call the author manager to create a new author
        author = self.author_manager.create_author(name, nationality)

        if author is not None:
            print(f"Author {author.name} ({author.nationality}) created with ID {author.author_id}.")
        else:
            print("Unable to create author. Please try again.")


class GenreUI:
    def __init__(self, genre_manager):
        self.genre_manager = genre_manager

    def create_genre(self):
        name = input("Enter Genre Name: ")

        # Call the genre manager to create a new genre
        genre = self.genre_manager.create_genre(name)

        if genre is not None:
            print(f"Genre {genre.name} created with ID {genre.genre_id}.")
        else:
            print("Unable to create genre. Please try again.")


class PublisherUI:
    def __init__(self, publisher_manager):
        self.publisher_manager = publisher_manager

    def create_publisher(self):
        name = input("Enter Publisher Name: ")
        location = input("Enter Publisher Location: ")

        # Call the publisher manager to create a new publisher
        publisher = self.publisher_manager.create_publisher(name, location)

        if publisher is not None:
            print(f"Publisher {publisher.name} ({publisher.location}) created with ID {publisher.publisher_id}.")
        else:
            print("Unable to create publisher. Please try again.")


class MemberUI:
    def __init__(self, member_manager):
        self.member_manager = member_manager

    def register_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        contact_info = input("Enter Contact Info: ")
        address = input("Enter Address: ")

        # Call the member manager to register a new member
        member = self.member_manager.register_member(member_id, name, contact_info, address)

        if member is not None:
            print(f"Member {member.name} registered with ID {member.member_id}.")
        else:
            print("Unable to register member. Please try again.")

    def remove_member(self):
        member_id = input("Enter Member ID to Remove: ")

        # Call the member manager to remove a member
        removed = self.member_manager.remove_member(member_id)

        if removed:
            print(f"Member with ID {member_id} removed successfully.")
        else:
            print(f"No member found with ID {member_id}.")
