# Posts & Comments API

This API provides CRUD functionality for posts and comments in a social media application.  
Built with **Django REST Framework (DRF)**.

---

## Authentication

All requests that modify data (create, update, delete) require authentication.  
Use **Token Authentication**:


---

## 📌 Posts Endpoints

### 1. List All Posts
**GET** `/api/posts/`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "author": "cyrus",
    "title": "My First Post",
    "content": "Excited to start building!",
    "created_at": "2025-08-18T10:15:00Z",
    "updated_at": "2025-08-18T10:15:00Z"
  }
]
```

### 2. Create a Post
**POST** `/api/posts/`

**Headers:**
```
Authorization: Token your_token_here
```
**Request:**
```bash
{
  "title": "My First Post",
  "content": "Excited to start building!"
}
```
**Response (201 Created):**
```json
{
  "id": 1,
  "author": "cyrus",
  "title": "My First Post",
  "content": "Excited to start building!",
  "created_at": "2025-08-18T10:15:00Z",
  "updated_at": "2025-08-18T10:15:00Z"
}
```
### 3. Retrieve a Single Post

**GET** `/api/posts/{id}/`

### Response (200 OK):
```json
{
  "id": 1,
  "author": "cyrus",
  "title": "My First Post",
  "content": "Excited to start building!",
  "created_at": "2025-08-18T10:15:00Z",
  "updated_at": "2025-08-18T10:15:00Z"
}
```
### 4. Update a Post

**PUT** `/api/posts/{id}/`

### Headers:
```
Authorization: Token your_token_here
```

### Request:
```json
{
  "title": "Updated Post Title",
  "content": "Updated content"
}
```

### Response (200 OK):
```json
{
  "id": 1,
  "author": "cyrus",
  "title": "Updated Post Title",
  "content": "Updated content",
  "created_at": "2025-08-18T10:15:00Z",
  "updated_at": "2025-08-18T12:30:00Z"
}
```
### 5. Delete a Post
**DELETE** `/api/posts/{id}/`

### Headers:
```
Authorization: Token your_token_here
```

### Response (204 No Content):
```
{}
```

## Comments Endpoints
### 1. List All Comments

**GET** `/api/comments/`

### Response (200 OK):
```json
[
  {
    "id": 1,
    "post": 1,
    "author": "cyrus",
    "content": "Nice post!",
    "created_at": "2025-08-18T11:00:00Z",
    "updated_at": "2025-08-18T11:00:00Z"
  }
]
```
### 2. Create a Comment

**POST** `/api/comments/`

### Headers:
```
Authorization: Token your_token_here
```

### Request:
```json
{
  "post": 1,
  "content": "Nice post!"
}
```

### Response (201 Created):
```json
{
  "id": 1,
  "post": 1,
  "author": "cyrus",
  "content": "Nice post!",
  "created_at": "2025-08-18T11:00:00Z",
  "updated_at": "2025-08-18T11:00:00Z"
}
```
### 3. Retrieve a Single Comment

**GET** `/api/comments/{id}/`

### Response (200 OK):
```json
{
  "id": 1,
  "post": 1,
  "author": "cyrus",
  "content": "Nice post!",
  "created_at": "2025-08-18T11:00:00Z",
  "updated_at": "2025-08-18T11:00:00Z"
}
```
### 4. Update a Comment

**PUT** `/api/comments/{id}/`

### Headers:
```
Authorization: Token your_token_here
```

### Request:
```json
{
  "post": 1,
  "content": "Really cool post!"
}
```

### Response (200 OK):
```json
{
  "id": 1,
  "post": 1,
  "author": "cyrus",
  "content": "Really cool post!",
  "created_at": "2025-08-18T11:00:00Z",
  "updated_at": "2025-08-18T11:30:00Z"
}
```
### 5. Delete a Comment

**DELETE** `/api/comments/{id}/`

### Headers:
```
Authorization: Token your_token_here
```

### Response (204 No Content):
```
{}
```