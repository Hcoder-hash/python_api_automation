import requests
import uuid
import os

class YunoAPI:

    def __init__(self):
        self.base_url = os.getenv("BASE_URL")

    def headers(self):
        return {
            "public-api-key": os.getenv("PUBLIC_API_KEY"),
            "private-secret-key": os.getenv("PRIVATE_SECRET_KEY"),
            "x-idempotency-key": str(uuid.uuid4()),
            "Content-Type": "application/json"
        }

    def create_purchase(self, payload):
        return requests.post(
            f"{self.base_url}/payments",
            json=payload,
            headers=self.headers()
        )
