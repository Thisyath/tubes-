import hashlib

def hash_password(password: str) -> str:
    """Hash password using SHA-256 (for simple use, not for production)."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against its hash."""
    return hash_password(password) == hashed