# Social Media API – Authentication & User Setup

This document explains how to set up authentication, register new users, log them in, and access protected endpoints in the Social Media API built with **Django** and **Django REST Framework (DRF)**.

---

## 1. Setup Process

### Install Dependencies
```bash
pip install djangorestframework djangorestframework-simplejwt
pip install pillow   # required for image uploads
```
### Add to `settings.py`
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]

AUTH_USER_MODEL = "accounts.CustomUser" #set custom user model

# Configure DRF authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# Run migrations
python manage.py makemigrations
python manage.py migrate

```
## Authentication Flow
- The API uses Token Authentication.
- When a user registers, a token is created.
- When a user logs in, their token is returned.
- For any protected endpoint, the client must send this token in the Authorization header.

## API Endpoints
### 1. Register

`POST` → /api/accounts/register/<br/>
Registers a new user.

### Request Body:
```bash
{
  "username": "alice",
  "email": "alice@example.com",
  "password": "1234",
  "bio": "Excited to join!"
}
```
### Response:
```bash
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "bio": "Excited to join!",
  "profile_picture": null,
  "followers_count": 0,
  "following_count": 0
}
```
### 2. Login

`POST` → /api/accounts/login/<br/>
Authenticates user and returns token.

### Request Body:
```bash
{
  "username": "alice",
  "password": "1234"
}
```
### Response:
```bash
{
  "username": "alice",
  "token": "a1b2c3d4e5f6g7h8..."
}
```
### 3. Profile

`GET` → /api/accounts/me/<br/>
Returns the currently logged-in user’s profile.
Requires token in the header.

<i>Headers:</i>
```
Authorization: Token a1b2c3d4e5f6g7h8...
```

### Response:
```bash
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "bio": "Excited to join!",
  "profile_picture": null,
  "followers_count": 0,
  "following_count": 0
}
```
## Testing with Postman
* Register a user with `/register/`.</br>
* Login with `/login/` and copy the token.</br>
* Use the token in the header for `/profile/`.</br>
Example header in Postman:
```
Authorization: Token a1b2c3d4e5f6g7h8...
```