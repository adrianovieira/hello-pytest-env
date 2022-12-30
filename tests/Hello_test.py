from fastapi.testclient import TestClient
import os


class TestHello:
    
    def test_get_main_index(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {'Hello': 'World'}


    def test_get_main_env_world_placeed(self, client_env: TestClient):
        response = client_env.get("/My World place")
        
        assert response.status_code == 200
        place = os.environ['APP_PLACE']
        assert response.json() == {'Hello': 'My World place', "place": place}