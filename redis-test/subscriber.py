import redis

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379)

pubsub = redis_client.pubsub()
pubsub.subscribe('channel')


for message in pubsub.listen():
    if message['type'] == 'message':
        print("Received message: " + message['data'].decode('utf-8'))
