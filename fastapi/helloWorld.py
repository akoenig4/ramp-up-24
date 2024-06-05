from fastapi import FastAPI  # noqa: E999

app = FastAPI()

@app.get('/{name}')
async def hello_world(name: str):
    return 'Hello ' + name