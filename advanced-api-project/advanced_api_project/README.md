## API Endpoints
- GET /api/books/ → List all books
- GET /api/books/<id>/ → Retrieve details for a specific book
- POST /api/books/create/ → Create a new book (requires authentication)
- PUT/PATCH /api/books/<id>/update/ → Update a book (requires authentication)
- DELETE /api/books/<id>/delete/ → Delete a book (requires authentication)

Permissions:
- Anyone can view books.
- Only authenticated users can create, update, or delete books.

## API Query Capabilities

### Filtering
- `/api/books/?author=Alice`
- `/api/books/?publication_year=2023`

### Searching
- `/api/books/?search=Django`

### Ordering
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`

