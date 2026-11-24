import hashlib
import secrets


def generate_key(prefix='sk'):
    raw = secrets.token_urlsafe(32)
    return prefix + '_' + raw


def hash_key(key):
    return hashlib.sha256(key.encode()).hexdigest()


def verify_key(key, stored_hash):
    return hash_key(key) == stored_hash
