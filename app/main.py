from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.models import Base
from app.api import user, incentive
from app.config import settings

# Создание экземпляра FastAPI
app = FastAPI()

# Настройка CORS (если необходимо)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Укажите разрешенные источники
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Регистрация маршрутов
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(incentive.router, prefix="/incentives", tags=["incentives"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Incentive Motivation API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
