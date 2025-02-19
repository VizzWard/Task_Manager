# Endopoints (local)

## Register

Endpoint: POST /accounts/register/

```curl
curl -X POST http://localhost:8000/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
        "email": "user@example.com",
        "name": "John Doe",
        "password": "securepassword123"
      }'
```

Respuesta:

```json
{
  "uuid": "1e6f4f2e-5d5e-46e6-9b3d-d5e6f4d5e6f4",
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securepassword123"
}
```

## Obtener Token de Acceso

Endpoint: POST /auth/token/

```curl
curl -X POST http://localhost:8000/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{
        "email": "user@example.com",
        "password": "securepassword123"
      }'
```

Respuesta:

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Refrescar Token de Acceso

Endpoint: POST /auth/token/refresh/

```curl
curl -X POST http://localhost:8000/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
        "refresh": "<your_refresh_token>"
      }'
```

Respuesta:

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Login

Endpoint: `POST /auth/login/`

```curl
curl -X POST http://localhost:8000/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
        "email": "user@example.com",
        "password": "securepassword123"
      }'
```

Respuesta:

```json
{
  "detail": "Successfully logged in"
}
```

## Logout

Endpoint: `POST /auth/logout/`

```curl
curl -X POST http://localhost:8000/auth/logout/ \
  -H "Authorization: Bearer <token_her>"
```

Respuesta:

```json
{
  "detail": "Successfully logged out"
}
```