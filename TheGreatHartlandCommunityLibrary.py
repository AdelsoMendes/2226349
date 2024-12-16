import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("Community Library")
    print(banner)
Book_list = [
    {"title": "The Book of Disquiet", "author": "Fernando Pessoa"},
    {"title": "The Lusiad", "author": "Luís Vaz Camões"},
    {"title": "The Lusiad", "author": "Luís Vaz Camões"},
    {"title": "The Maias",  "author": "Eça de Queirós"},
    {"title": "The Crime of Father Amaro", "author": "Eça de Queirós"},
    {"title": "Blindness", "author": "José Saramago"},
    {"title": "Nos Matamos O Cão Tinhoso", "author": "Bernardo Honwana"},
    {"title": "Signs Of Fire", "author": "Jorge de Sena"},
    {"title": "Karingana Ua Karingana", "author":"José Craveirinha"},
    {"title": "The Return Of The Caravels", "author": "António Lobo Antunes"},
    {"title": "Sleepwalking Land", "author": "Mia Couto"}
]
def book_management_menu():
    while True:
        print("\nBook Record Management")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Exit")
        action = input("Choose an action: ")
        match action:
            case '1':
                add_book()
            case '2':
                remove_book()
            case '3':
                return
            case _:
                print("Invalid option, please try again.")
def add_book():
    title = input("Enter the title of the book to add:")
    # Logic to add the book (e.g., append to a list or database)
    print(f"Book '{title}' added successfully.")
def remove_book():
    title= input("Enter the title of the book to remove:")
    #Logic to remove book
    print(f"book '{title}') remove successfully.")
def search_by_title_menu():
    while True:
        print("\nBook Searching")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Exit")
        search_type = input("Choose a search type:")
        match search_type:
            case '1':
                search_by_title()
            case '2':
                search_by_author()
            case '3':
                return
            case _:
                print("invalid option, please try again.")
def search_by_title():
    title = input("Enter the title to search: ")
    #logic to search by title
    print(f"Search for a book with title '{title}...")
    result = []
    for book in Book_list:
        if title.lower() in book['title'].lower():
            result.append(book)
    if result:
        print("\n Result:")
        for idx, book in enumerate(result, 1):
            print(f"{idx}. {book['title']} - {book['author']}")
    else:
        print("\n Result no found")
def search_by_author():
    author= input("Enter the author to search: ")
    #Logic to search by author
    print(f"Searching for book by author '{author}'...")
    result = []
    for book in Book_list:
        if author.lower() in book['author'].lower():
            result.append(book)
    if result:
        print("\n Result:")
        for idx, book in enumerate(result, 1):
            print(f"{idx}. {book['title']} - {book['author']}")
    else:
        print("\n Result no found")
def display_results():
    print("Display search results...")
    #Logic to display search results
def check_out_check_in_menu():
    while True:
        print("\nCheck-In and Check -Out")
        print("1. Check-Out")
        print("2. Check-In")
        print("3. Exit")
        check_action = input("Choose an action:")
        match check_action:
            case '1':
                check_out()
            case '2':
               check_in()
            case '3':
                return
            case _:
                print("invalid option, please try again.")
def check_out():
    title = input("Enter the title of the book to check out: ")
    #Logic to check out the update_record()
    print("fBook '{title}' check out successfully.")
def check_in():
    title = input("Enter the title of the book to check in: ")
    #Logic to check in book update_records()
    print("fBook '{title}' check in successfully")
def update_reports():
    #Logic to update records after check-in or check-out
    print(" Records updated Successfully.")
def view_reports():
    # Logic to view reports
    print("Viewing reports...")
def main_menu():
    print_banner()
    while True:
        print("\nMain Menu")
        print("1. Book Record Management")
        print("2. Book Searching")
        print("3. Check-In And Check-Out")
        print("4. Basic Reporting")
        print("5. Exit")

        choice = input("Chose an option:")
        match choice:
            case '1':
                book_management_menu()
            case '2':
                search_by_title_menu()
            case '3':
                check_out_check_in_menu()
            case '4':
                view_reports()
            case '5':
                print("Exiting...")
                break
            case _:
                print("Invalid option, please try agin.")
if __name__ == "__main__":
    main_menu()