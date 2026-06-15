from fastapi import FastAPI

from models import PasswordRequest
from password_checker import check_strength
from password_generator import generate_password
from breach_scanner import is_breached

app = FastAPI()

@app.post("/check-password")
def check_password(request: PasswordRequest):

    return {
        "strength": check_strength(request.password),
        "breached": is_breached(request.password)
    }

@app.get("/generate-password")
def generate():

    password = generate_password()

    return {
        "password": password,
        "strength": check_strength(password)
    }