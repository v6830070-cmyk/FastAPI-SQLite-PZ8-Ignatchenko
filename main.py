from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from database.connection import conn

# Импортируем словарь users из твоего файла users.py
from routes.users import user_router, users 
from routes.events import event_router

import uvicorn

app = FastAPI(title="Planner API (SQLite) — Игнатченко Владислав")

templates = Jinja2Templates(directory="templates")

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

@app.get("/admin")
async def admin_panel(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"users": users}
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)