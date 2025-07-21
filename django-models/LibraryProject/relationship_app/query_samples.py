from relationship_app.models import Library, Book, Author

# Query 1: Retrieve all books for a specific library.
library_name = "Some Library Name"
books_in_library = Library.objects.get(name=library_name).books.all()

# Query 2: Retrieve all books by a specific author in two steps.
author_name = "Some Author Name"
author = Author.objects.get(name=author_name)            # This line is required!
books_by_author = Book.objects.filter(author=author)       # And this line too!

# Query 3: Retrieve the librarian for a specific library.
librarian = Library.objects.get(name=library_name).librarian

