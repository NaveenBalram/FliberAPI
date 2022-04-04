import numpy as np
from cryptography.fernet import Fernet
import numpy_financial as npf


def encrypt_data(message):
    """Encrypt the data.

    return: key, encrypted message
    """

    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())

    return key, encMessage


def decrypt_data(key, message):
    """Decrypt the data."""
    fernet = Fernet(key)
    decMessage = fernet.decrypt(message).decode()

    return decMessage
