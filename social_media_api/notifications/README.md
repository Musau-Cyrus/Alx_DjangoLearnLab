# Likes & Notifications API Documentation

This section documents how users can like/unlike posts and receive notifications for important activities. These features enhance user engagement and create a more interactive experience within the social media platform.

## Likes
### 1. Like a Post
### Endpoint:
`POST /posts/<post_id>/like/`

### Description:
Allows an authenticated user to like a specific post. If the post is already liked by the user, the system prevents duplicate likes.

### Request Headers:
```
Authorization: Token <your-auth-token>
Content-Type: application/json
```

### Response Example (Success):
```json
{
  "message": "Post liked successfully."
}
```

### Response Example (Already Liked):
```json
{
  "detail": "You have already liked this post."
}
```
### 2. Unlike a Post
**Endpoint:**

`POST /posts/<post_id>/unlike/`

### Description:
Allows an authenticated user to remove their like from a post.

### Request Headers:
```
Authorization: Token <your-auth-token>
Content-Type: application/json
```

### Response Example (Success):
```json
{
  "message": "Post unliked successfully."
}
```

### Response Example (Not Liked Yet):
```json
{
  "detail": "You have not liked this post."
}
```
## Notifications

Notifications keep users updated about important activities such as:
- A new follower
- Someone liking their post
- Someone commenting on their post

## 1. View Notifications
**Endpoint:**
```
GET /notifications/
```

### Description:
Fetches a list of notifications for the logged-in user, ordered by newest first.

### Request Headers:
```
Authorization: Token <your-auth-token>
```

### Response Example:
```json
[
  {
    "id": 1,
    "recipient": "john_doe",
    "actor": "jane_smith",
    "verb": "liked your post",
    "target": "Post: My First Blog",
    "timestamp": "2025-08-24T13:45:00Z",
    "read": false
  },
  {
    "id": 2,
    "recipient": "john_doe",
    "actor": "alex_m",
    "verb": "started following you",
    "target": null,
    "timestamp": "2025-08-24T12:10:00Z",
    "read": true
  }
]
```
