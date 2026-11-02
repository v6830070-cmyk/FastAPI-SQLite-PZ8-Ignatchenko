from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from database.connection import conn

# Импортируем роутеры и словарь пользователей
from routes.users import user_router, users 
from routes.events import event_router

import uvicorn

app = FastAPI(title="Planner API (SQLite) — Игнатченко Владислав")

# Подключаем папку с HTML-шаблонами
templates = Jinja2Templates(directory="templates")

# Подключаем маршруты API
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# Создание базы данных при запуске
@app.on_event("startup")
def on_startup():
    conn()

# Редирект с главной страницы на события
@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

# Маршрут для админ-панели (скрыт из Swagger)
@app.get("/admin", include_in_schema=False)
async def admin_panel(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"users": users}
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)