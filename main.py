from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()


class UsuarioLogin(SQLModel):
    userName: str
    password: str


user_db = [
    UsuarioLogin(userName="admin", password="password123"),
    UsuarioLogin(userName="user1", password="1234")
]



@app.post("/login")
def login(usuario: UsuarioLogin):
    for user in user_db:
        if user.userName == usuario.userName and user.password == usuario.password:
            return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
