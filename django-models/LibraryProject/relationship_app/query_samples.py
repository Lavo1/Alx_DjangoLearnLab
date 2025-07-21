from relationship_app.models import Library, Book, Author

# ✅ 1. List all books in a library
library_name = "Some Library Name"
books_in_library = Library.objects.get(name=library_name).books.all()

# ✅ 2. Query all books by a specific author
author_name = "Some Author Name"
books_by_author = Book.objects.filter(author__name=author_name)

# ✅ 3. Retrieve the librarian for a library
library_name = "Some Library Name"
librarian = Library.objects.get(name=library_name).librarian

