"""redis publisher module"""
import redis
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379)



class Message(BaseModel):
    """message class"""
    message: str

@app.post("/publish/")
async def pub(message: Message):
    """Function publishing message to redis channel."""
    redis_client.publish('channel', message.message)
    return {"status": "Message published"}
