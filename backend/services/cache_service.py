import redis
from backend.config import settings

r = redis.Redis.from_url(settings.REDIS_URL)

def set_cache(key, value, ttl=3600):
    r.set(key, value, ex=ttl)

def get_cache(key):
    val = r.get(key)
    return val.decode() if val else None

async def get_health_status():
    try:
        pong = r.ping()
        return {"redis": "ok" if pong else "down"}
    except:
        return {"redis": "error"}
