# Social Media API – Follow & Feed Features

This section documents the follow system and the user feed functionality.  
It builds on top of the Posts & Comments features.

---

## Follow System

### Endpoints

## 1. Follow a User
- **URL:** `/api/accounts/follow/<username>/`
- **Method:** `POST`
- **Auth Required:** Yes (Token)
- **Description:** Logged-in user follows the given `<username>`.

**Example Request:**
```http
POST /api/accounts/follow/alice/
Authorization: Token <your_token>
```
### Example Response:
```josn
{
  "detail": "You are now following alice."
}
```
## 2. Unfollow a User

- URL: 
`/api/accounts/unfollow/<username>/`
- Method: `POST`
- Auth Required: Yes `(Token)`
- Description: Logged-in user unfollows the given `<username>`.

### Example Request:
```
POST /api/accounts/unfollow/alice/
Authorization: Token <your_token>
```

### Example Response:
```json
{
  "detail": "You have unfollowed alice."
}
```
## 3. List a User’s Followers
- URL: `/api/accounts/followers/<username>/`
- Method: `GET`
- Auth Required: Yes `(Token)`
- Description: Get all followers of the given `<username>`.
### Example Request:
```
GET /api/accounts/followers/alice/
Authorization: Token <your_token>
```

### Example Response:
```json
{
  "followers": ["bob", "charlie"]
}
```
## 4. List Users a Person is Following
- URL: `/api/accounts/following/<username>/`
- Method: `GET`
- Auth Required: Yes `(Token)`
- Description: Get all users that `<username>` is following.

### Example Request:
```
GET /api/accounts/following/bob/
Authorization: Token <your_token>
```

### Example Response:
```json
{
  "following": ["alice", "charlie"]
}
```

# Feed
The feed shows posts from users that the logged-in user follows, ordered by most recent.

## Endpoint
### Get User Feed
- URL: `/api/posts/feed/`
- Method: `GET`
- Auth Required: Yes `(Token)`
- Description: Returns posts created by users the logged-in user follows.

### Example Request:
```
GET /api/posts/feed/
Authorization: Token <your_token>
```

### Example Response:
```json
[
  {
    "id": 12,
    "author": "alice",
    "title": "My first post!",
    "content": "Hello world 🌍",
    "created_at": "2025-08-20T10:15:00Z",
    "updated_at": "2025-08-20T10:15:00Z"
  },
  {
    "id": 11,
    "author": "charlie",
    "title": "Good vibes only",
    "content": "Enjoying some coffee ☕",
    "created_at": "2025-08-19T09:45:00Z",
    "updated_at": "2025-08-19T09:45:00Z"
  }
]
```