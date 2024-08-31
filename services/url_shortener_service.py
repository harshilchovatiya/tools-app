import hashlib
from utils.mongo_client import urls_collection

def generate_short_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    short_hash = hash_object.hexdigest()[:6]
    return short_hash

def store_url(short_url, long_url):
    existing_entry = urls_collection.find_one({'long_url': long_url})
    
    if existing_entry:
        # If the long URL exists, return the existing short URL
        return existing_entry['short_url']
    else:
        urls_collection.update_one(
            {'short_url': short_url},
            {'$set': {'long_url': long_url}},
            upsert=True
        )

def get_long_url(short_url):
    result = urls_collection.find_one({'short_url': short_url})
    if result:
        return result.get('long_url')
    return None

