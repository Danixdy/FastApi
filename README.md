Endpoint /login

Método: POST

Body (JSON):

{
  "userName": "admin",
  "password": "password123"
}


Respuestas posibles:

Login exitoso:

{
  "message": "Login successful"
}


Credenciales inválidas:

{
  "message": "Invalid credentials"
}
