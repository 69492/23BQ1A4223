from fastapi import APIRouter, HTTPException
from app.services.notification_service import NotificationService

router = APIRouter()

@router.get("/notifications")
def get_notifications():
    try:
        return NotificationService.get_notifications()
    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))