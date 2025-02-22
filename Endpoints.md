# Local Endpoints

## Users

### Register

**POST http://localhost:8000/accounts/register/**

Request:

```json
{
    "username": "user",
    "email": "email@email.com",
    "password": "password"
}
```

Response:

```json
{
    "message": "User created successful"
}
```

---

### Login

**POST http://localhost:8000/accounts/login/**

Request:

```json
{
    "email": "testuser4@gmail.com",
    "password": "testpassword"
}
```

Response:

```json
{
    "tokens": {
        "refresh": "eyJhbGciOiJIUzI...",
        "access": "eyJhbGciOiJIUzI1..."
    }
}
```

---

### Logout

**POST http://localhost:8000/accounts/logout/**

Request (Autorization header with Bearer token):

```json
{
    "refresh": "eyJhbGciOiJIUzI..."
}
```

---

Response:

```json
{
    "message": "Logout success"
}
```

---

### Refresh Token

**POST http://localhost:8000/accounts/api/token/refresh/**

Request:

```json
{
    "refresh": "eyJhbGciOiJIUzI..."
}
```

Response:

```json
{
    "access": "eyJhbGciOiJI..."
}
```

---

### User Settings

**GET http://localhost:8000/accounts/settings/**

Request (Autorization header with Bearer token):

```json
{}
```

Response:

```json
{
    "notification": true,
    "night_mode": false
}
```

---

### Update User Settings

**PUT http://localhost:8000/accounts/settings/**

Request (Autorization header with Bearer token) `No one requiered`:

```json
{
    "notification": false,
    "night_mode": true
}
```

Response:

```json
{
    "success": true,
    "id": 5,
    "notification": false,
    "night_mode": true
}
```

---

## Tasks

### Create Task

**POST http://localhost:8000/task/create/**

Request (Autorization header with Bearer token) `Only task_name requiered`:


```json
{
    "task_name": "test_task_4",
    "task_description": "",
    "progress": 0,
    "priority": false,
    "start_date": null,
    "end_date": null,
    "tag_name": "pruebas"
}
```

Response:

```json
{
    "id": 13,
    "name": "test_task_5",
    "description": "prueba5",
    "progress": 0,
    "priority": false,
    "start_date": "2025-02-21T14:04:56.563465Z",
    "end_date": null,
    "state": true,
    "created_at": "2025-02-21T14:04:56.569609Z",
    "modified_at": null,
    "tag_name": "pruebas2"
}
```

---

### Get Filtered/Ordering Tasks

Filter by: 
- `all=true`: Get history tasks [Extra field `state` return | true: active, false: inactive]
- `tag_name`: Filter by tag name [If `tag_name` is null return all tasks | `tag_name=<tag_name>` return only tasks with the tag name]
- `priority=true`: Filter by priority [If `priority=false` return all tasks | `priority=true` return only priority tasks]

Order by (add `-` for descending order):
- `created_at`: Orber by created date (Default)
- `name`: Order by name (Alphabetic)
- `progress`: Order by progress (Numeric order 0-6)
- `start_date`: Order by start date
- `end_date`: Order by end date

Get active tasks (no paramns):
**GET http://localhost:8000/task/get_tasks/** 

Example with params (only one ordering field):

**GET http://localhost:8000/task/get_tasks/?all=true&tag_name=pruebas&priority=true&ordering=end_date**

Request (Autorization header with Bearer token):

```json
{}
```

Response:

```json
[
    {
        "id": 1,
        "name": "task_task",
        "progress": 3,
        "priority": true,
        "tag_name": "tasks",
        "created_at": "2025-02-21T03:27:15.078461Z",
        "state": false
    },
    {
        "id": 2,
        "name": "test_task",
        "progress": 0,
        "priority": false,
        "tag_name": null,
        "created_at": "2025-02-21T03:27:15.081962Z",
        "state": true
    }
]
```

---

### Get Task by ID

**GET http://localhost:8000/task/get_task/1**

Request (Autorization header with Bearer token):

```json
{}
```

Response:

```json
{
    "task": {
        "id": 1,
        "name": "test_task",
        "description": "",
        "progress": 0,
        "priority": false,
        "start_date": "2025-02-21T03:27:15.077963Z",
        "end_date": null,
        "state": true,
        "created_at": "2025-02-21T03:27:15.078461Z",
        "modified_at": null,
        "tag_name": null
    }
}
```

---

### Update Task

**PUT http://localhost:8000/task/update_task/1**

Request (Autorization header with Bearer token) `Only task_name requiered`:

```json
{
    "task_name": "task_task",
    "task_description": "mod",
    "progress": 3,
    "priority": true,
    "start_date": null,
    "end_date": null,
    "state": false,
    "tag_name": "tasks"
}
```

Response:

```json
{
    "id": 1,
    "name": "task_task",
    "description": "mod",
    "progress": 3,
    "priority": true,
    "start_date": "2025-02-21T03:27:15.077963Z",
    "end_date": null,
    "state": false,
    "created_at": "2025-02-21T03:27:15.078461Z",
    "modified_at": "2025-02-21T14:18:42.689784Z",
    "tag_name": "tasks"
}
```

---

### Delete Task

**DELETE http://localhost:8000/task/update_task/1**

Request (Autorization header with Bearer token):

```json
{}
```

Response:

```json
{
    "message": "Tarea eliminada correctamente."
}
```

---

## Comments

### Create Comment on task

**POST http://localhost:8000/task/comment/1**

Request (Autorization header with Bearer token):

```json
{
    "comment": "test comment"
}
```

Response:

```json
{
    "id": 1,
    "comment": "test comment",
    "created_at": "2025-02-21T12:39:47.346079Z"
}
```

---

### Get Comments on task

**GET http://localhost:8000/task/get_comments/9**

Request (Autorization header with Bearer token):

```json
{}
```

Response:

```json
[
    {
        "id": 1,
        "comment": "test comment",
        "created_at": "2025-02-21T12:36:01.663255Z"
    },
    {
        "id": 2,
        "comment": "test comment",
        "created_at": "2025-02-21T12:37:10.790693Z"
    }
]
```

---

### Update Comment

**PUT http://localhost:8000/task/comment/9/1**

Request (Autorization header with Bearer token):

```json
{
    "comment": "test comment update"
}
```

Response:

```json
{
    "id": 1,
    "comment": "test comment update",
    "created_at": "2025-02-21T12:36:01.663255Z"
}
```

---

### Delete Comment

**DELETE http://localhost:8000/task/comment/9/1**

Request (Autorization header with Bearer token):

```json
{}
```

Response:

```json
{
    "message": "Comentario eliminado correctamente."
}
```