

from fastapi.testClient import TestClient
from app.main import app

Client = TestClient(app)

def test_home():
  response = Client.get('/')
  assert response.status_code == 200