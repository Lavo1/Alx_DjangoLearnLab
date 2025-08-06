from relationship_app.models import Library, Book, Author, Librarian

# ✅ 1. List all books in a library
library_name = "Some Library Name"
books_in_library = Library.objects.get(name=library_name).books.all()

# ✅ 2. Query all books by a specific author
author_name = "Some Author Name"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# ✅ 3. Retrieve the librarian for a library (this exact structure matters!)
librarian = Librarian.objects.get(library=Library.objects.get(name=library_name))
