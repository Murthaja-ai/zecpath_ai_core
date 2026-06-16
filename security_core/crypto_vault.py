# security_core/crypto_vault.py
import os
from cryptography.fernet import Fernet

class CryptoVault:
    KEY_FILE = "security_core/.env.secret"

    @classmethod
    def _get_or_create_key(cls) -> bytes:
        """Retrieves a persistent encryption key to prevent data loss across server reboots."""
        if os.path.exists(cls.KEY_FILE):
            with open(cls.KEY_FILE, "rb") as f:
                return f.read()
        else:
            # Generate key once and lock it down
            key = Fernet.generate_key()
            with open(cls.KEY_FILE, "wb") as f:
                f.write(key)
            return key

    @classmethod
    def encrypt_transcript(cls, raw_text: str) -> bytes:
        """Encrypts highly sensitive PII data."""
        cipher = Fernet(cls._get_or_create_key())
        return cipher.encrypt(raw_text.encode('utf-8'))

    @classmethod
    def decrypt_transcript(cls, encrypted_token: bytes) -> str:
        """Decrypts data back to human-readable text for authorized viewers."""
        cipher = Fernet(cls._get_or_create_key())
        return cipher.decrypt(encrypted_token).decode('utf-8')