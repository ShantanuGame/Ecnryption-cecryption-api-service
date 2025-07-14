from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Load or create the key
def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    return key

# Load key on module import
key = load_or_generate_key()
cipher = Fernet(key)

# Encrypt function
def encrypt_text(plain_text: str) -> str:
    return cipher.encrypt(plain_text.encode()).decode()

# Decrypt function
def decrypt_text(encrypted_text: str) -> str:
    return cipher.decrypt(encrypted_text.encode()).decode()
