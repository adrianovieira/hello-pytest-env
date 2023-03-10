from fastapi.testclient import TestClient
import os
import pytest


@pytest.fixture()
def client():
    from main import app

    yield TestClient(app)
    

@pytest.fixture()
def client_env(request):
    
    os.environ['APP_PLACE'] = 'EU' if not hasattr(request, 'param') else request.param
    
    from main import app as app_env
    
    yield TestClient(app_env)
