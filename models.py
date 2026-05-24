from pydantic import BaseModel, EmailStr

class LoginForm(BaseModel):
    correo: EmailStr
    password: str

class Student(BaseModel):
    correo: str
    password: str
    nombre: str