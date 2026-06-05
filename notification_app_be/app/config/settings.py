from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

print("BASE_URL =", BASE_URL)
print("TOKEN FOUND =", AUTH_TOKEN is not None)
print("TOKEN START =", AUTH_TOKEN[:20] if AUTH_TOKEN else None)