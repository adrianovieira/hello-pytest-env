from fastapi.testclient import TestClient
import os
import pytest

class TestHello:
    
    def test_get_main_index(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {'Hello': 'World'}

    def test_get_main_world_placed(self, client: TestClient, monkeypatch):
        monkeypatch.setenv('APP_PLACE', 'ASIA')
        response = client.get("/My World place")
        
        assert response.status_code == 200
        app_place = os.environ['APP_PLACE']
        assert response.json() == {'Hello': 'My World placed ASIA', "place": app_place}
        
    def test_get_main_env_world_placed(self, client_env: TestClient):
        response = client_env.get("/My World place")
        
        assert response.status_code == 200
        app_place = os.environ['APP_PLACE']
        assert response.json() == {'Hello': 'My World placed EU', "place": app_place}

        
    @pytest.mark.parametrize("client_env", ["AMERICA"], indirect=True)
    def test_get_main_env_world_placed_parametrize(self, client_env: TestClient):
        response = client_env.get("/My World place")
        
        assert response.status_code == 200
        app_place = os.environ['APP_PLACE']
        assert response.json() == {'Hello': 'My World placed AMERICA', "place": app_place}
        