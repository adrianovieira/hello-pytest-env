from fastapi import FastAPI

from app.config import CONFIG

app = FastAPI()

@app.get("/")
def hello():
    return {'Hello': 'World'}


@app.get("/{env_world}")
def hello_env_world(env_world: str):
    place = CONFIG.PLACE
    result = {"Hello": env_world} if not place else {"Hello": env_world, "place": place}
    return result

