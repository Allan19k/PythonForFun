from cryptography.fernet import Fernet 

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Sensitive Cybersecurity Data"
# Encrypt the message
encrypted_message = cipher.encrypt(message)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message.decode())
