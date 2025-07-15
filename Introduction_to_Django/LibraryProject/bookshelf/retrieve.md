# Retrieve the Book instance

```python
from bookshelf.models import Book

# Retrieve the created book
book = Book.objects.get(title="1984")
print(book)

# Expected output:
# 1984 by George Orwell (1949)
