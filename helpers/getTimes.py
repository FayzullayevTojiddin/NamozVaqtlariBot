import httpx
from .getRegionName import get_region_name_by_id
from helpers.toLatin import to_latin_only
from datetime import datetime, date
cache = {}

def get_cache_key(region_name):
    return f"{region_name}_{date.today().isoformat()}"

async def get_prayer_times(user):
    region_name = to_latin_only(get_region_name_by_id(user.region))
    key = get_cache_key(region_name)

    if key in cache:
        return cache[key]

    url = f"https://islomapi.uz/api/present/day?region={region_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    cache[key] = data
    return data