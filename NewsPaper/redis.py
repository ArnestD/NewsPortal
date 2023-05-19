import redis


red = redis.Redis(
    host='redis-17832.c256.us-east-1-2.ec2.cloud.redislabs.com',
    port='17832',
    password='06U2JgV7awDPcsyngF1DCKJ3F4pSDCwF'
)

# python -i redis.py
# red.set('ima','peremenaa')
# red.get('ima')