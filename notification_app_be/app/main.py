from fastapi import FastAPI

from app.routes.notification_routes import router
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI(
    title="AffordMed Notification API",
    version="1.0.0"
)


@app.middleware("http")
async def log_requests(request, call_next):

    middleware = LoggingMiddleware()

    return await middleware(request, call_next)


app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Backend Running"
    }