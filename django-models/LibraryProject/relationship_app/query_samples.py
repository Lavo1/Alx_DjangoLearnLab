from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (replace author_name as needed)
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return []

# 2. List all books in a library (replace library_name as needed)
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library (replace library_name as needed)
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage (if running in Django shell or with proper Django context):
if __name__ == '__main__':
    # Replace 'Alice' and 'Central Library' with actual values in your database
    print("Books by Alice:", list(books_by_author('Alice')))
    print("Books in Central Library:", list(books_in_library('Central Library')))
    print("Librarian for Central Library:", librarian_for_library('Central Library'))
