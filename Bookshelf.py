from Classes.Book import Book

class Bookshelf:
    """Creates a Bookshelf object that stores and manages cook books."""
    
    def __init__(self):
        self.bookshelf = []
        self.art = """
         ____           _                         
        |  _ \ ___  ___(_)_ __   ___              
        | |_) / _ \/ __| | '_ \ / _ \             
        |  _ <  __/ (__| | |_) |  __/             
        |_| \_\___|\___|_| .__/ \___|             
        |  \/  | __ _ _ _|_| __ _  __ _  ___ _ __ 
        | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
        | |  | | (_| | | | | (_| | (_| |  __/ |   
        |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                  |___/           
        """

    def add_book(self):
            """Method to add a book to the bookshelf."""
            
            print("Please enter cook book details:\n")
            
            book = Book()
            book.prompt()
            
            self.bookshelf.append(book)
    
    def view_book(self, book):
        """Method to get cook book from the book shelf and print recipe list to console."""
        
        self.bookshelf[int(book)].print_menu()

    def delete_book(self, book):
        """Method to delete cook book from bookshelf."""
        
        del self.bookshelf[int(book)]
        
    def print_art(self):
        """Method to print logo art to console."""
        
        print(self.art)

    def print_menu(self):
        """Method to print menu to console."""
        
        # TODO: Create menu options for managing cook books in bookshelf
        pass
    
    def prompt(self):
        """Prompts user to input recipe book details."""
        
        # TODO: For loop to run program
        
        # TODO: Print the menu options
        
        # TODO: Get option number
        
        # TODO: Get recipe book menu
        
        pass
