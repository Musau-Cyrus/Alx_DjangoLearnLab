## Detailed CRUD Operation

### 1. Create
new_book = Book(title = "1984", author = "George Orwell", publication_year = 1949)

### 2. Retrieve
books = Book.object.all()

### 3. Update
Book.objects.filter(id=1).update(title="Nineteen Eighty Four")