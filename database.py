USERS_DB: dict = {
    "hola@gmail.com": {
        "correo": "hola@gmail.com",
        "password": "1234",
        "nombre": "Usuario",
    }
}

def get_user(correo: str) -> dict | None:
    return USERS_DB.get(correo.strip().lower())

def verify_password(user: dict, password: str) -> bool:
    return user["password"] == password