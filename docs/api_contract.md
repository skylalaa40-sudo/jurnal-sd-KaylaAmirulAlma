# API Contract - User Profile
**Endpoint:** `/api/v1/profile`
**Method:** `GET`
**Response Body (JSON):**
{
"id": 1,
"username": "mahasiswa_sd",
"email": "mhs@univ.ac.id",
"avatar_url": "[https://image.com/avatar.png](https://image.com/avatar.png)"
}

# Login User

**Endpoint:** `/api/v1/login`

**Method:** `POST`

## Request Body

```json
{
  "email": "mhs@univ.ac.id",
  "password": "12345678"
}
```

## Response Body

```json
{
  "status": "success",
  "message": "Login berhasil",
  "token": "jwt_token_example",
  "user": {
    "id": 1,
    "username": "mahasiswa_sd",
    "email": "mhs@univ.ac.id"
  }
}
```