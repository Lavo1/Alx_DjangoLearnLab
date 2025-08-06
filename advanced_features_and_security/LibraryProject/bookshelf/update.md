
---

### 📄 `update.md` – 🛠 Change the book title

```markdown
# Update the Book title

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# Expected output:
# Nineteen Eighty-Four by George Orwell (1949)