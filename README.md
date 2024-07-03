# Blog

## Auth

### Register

- Endpoint: `127.0.0.1:8000/api/register`
- Method: `POST`
- Body:

```json
{
    "username": "username",     // required
    "password": "password",     // required
    "email": "email",
}
```

- Response:

```json
{
    "id": 1,
    "posts": [],
    "password": "hashed password",
    "last_login": null,
    "is_superuser": false,
    "username": "username",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2024-07-03T01:54:15.571975Z",
    "groups": [],
    "user_permissions": []
}
```

## Login

- Endpoint: `127.0.0.1:8000/api/login`
- Method: `POST`
- Body:

```json
{
    "username": "username",     // required
    "password": "password",     // required
}
```

- Response:

```json
{
    "refresh": "refresh jwt token",
    "access": "access jwt token"
}
```

## Categories

### Create Category

- Endpoint: `127.0.0.1:8000/api/categories`
- Method: `POST`
- Body:

```json
{
    "name": "name"
}
```

- Response:

```json
{
    "id": 1,
    "name": "name"
}
```

### Update Category

- Endpoint: `127.0.0.1:8000/api/categories/{category_id}`
- Method: `PUT`
- Body:

**Note:** Same request body and response

### Delete Category

- Endpoint: `127.0.0.1:8000/api/categories/{category_id}`
- Method: `DELETE`

**Note:** 204 status code when successfully deleted

### List Category

- Endpoint: `127.0.0.1:8000/api/categories`
- Method: `GET`
- Response:

```json
{
    "id": 1,
    "name": "name"
}
```

### Retrieve Category

- Endpoint: `127.0.0.1:8000/api/categories/{category_id}`
- Method: `GET`
- Response:

**Note:** Same response

## Posts

### Create Post

- Endpoint: `127.0.0.1:8000/api/posts`
- Method: `POST`
- Body:

```json
{
    "title": "title",
    "content": "content",
    "author": 1,
    "categories": [
        1
    ]
}
```

- Response:

```json
{
    "id": 1,
    "title": "aa123",
    "content": "aa1234",
    "created_at": "2024-07-03T02:18:27.908064Z",
    "updated_at": "2024-07-03T02:18:27.908204Z",
    "author": 1,
    "categories": [
        1
    ]
}
```

### Update Post

- Endpoint: `127.0.0.1:8000/api/posts/{post_id}`
- Method: `PUT`

**Note:** Same request body and response

### Delete Post

- Endpoint: `127.0.0.1:8000/api/posts/{post_id}`
- Method: `DELETE`

**Note:** 204 status code when successfully deleted

### Get Posts

- Endpoint: `127.0.0.1:8000/api/posts`
- Method: `GET`
- Pagination key: `page:1`
- Search key: `title:test`
- Response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "aa123",
            "content": "aa1234",
            "created_at": "2024-07-03T02:18:27.908064Z",
            "updated_at": "2024-07-03T02:18:27.908204Z",
            "author": 1,
            "categories": [
                1
            ]
        }
    ]
}
```

## Comments

### Create Comment

- Endpoint: `127.0.0.1:8000/api/posts/1/comments`
- Method: `POST`
- Body:

```json
{
    "author": 1,
    "post": 1,
    "content": "content"
}
```

- Response:

```json
{
    "author": 1,
    "post": 1,
    "content": "content"
}
```

### Get Posts Comments

- Endpoint: `127.0.0.1:8000/api/posts/1/comments`
- Method: `GET`
- Pagination key: `page:1`
- Response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "content": "content",
            "created_at": "2024-07-03T02:22:05.594216Z",
            "post": 1,
            "author": 1
        }
    ]
}
```

### Retrieve Comment

- Endpoint: `127.0.0.1:8000/api/posts/1/comments`
- Method: `GET`
- Response:

**Note:** Same response

### Update Comment

- Endpoint: `127.0.0.1:8000/api/comments/{post_id}`
- Method: `PUT`

**Note:** Same request body and response

### Delete Comment

- Endpoint: `127.0.0.1:8000/api/comments/{post_id}`
- Method: `DELETE`

**Note:** 204 status code when successfully deleted

### Get Comments

- Endpoint: `127.0.0.1:8000/api/comments`
- Method: `GET`
- Pagination key: `page:1`
- Search key: `content:test`
- Response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "content": "aaa",
            "created_at": "2024-07-03T02:40:46.396962Z",
            "post": 2,
            "author": 1
        }
    ]
}
```
