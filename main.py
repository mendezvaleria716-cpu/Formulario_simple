from pathlib import Path
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_user, verify_password

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="ATLAS")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    user = get_user(email)

    if not user or not verify_password(user, password):
        return RedirectResponse(url="/", status_code=303)

    user["nombre"] = email.strip().split("@")[0].capitalize()

    return RedirectResponse(url=f"/base?correo={email.strip().lower()}", status_code=303)

@app.get("/base", response_class=HTMLResponse)
async def home(request: Request, correo: str):
    user = get_user(correo)
    if not user:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse(
        request,
        "base.html",
        {"student": user},
    )

@app.get("/logout")
async def logout():
    return RedirectResponse(url="/", status_code=303)