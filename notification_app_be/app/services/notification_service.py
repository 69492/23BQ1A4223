import requests
from app.config.settings import BASE_URL, AUTH_TOKEN


class NotificationService:

    @staticmethod
    def get_notifications():

        headers = {
            "Authorization": f"Bearer {AUTH_TOKEN}",
            "Accept": "application/json"
        }

        try:
            response = requests.get(
                f"{BASE_URL}/notifications",
                headers=headers,
                timeout=10
            )

            return {
                "status_code": response.status_code,
                "response": response.text
            }

        except Exception as e:
            return {
                "error": str(e)
            }