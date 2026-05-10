from cryptography.fernet import Fernet
import os

# Lê chave
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

folder = "test_files"

for filename in os.listdir(folder):
    path = os.path.join(folder, filename)

    if os.path.isfile(path):
        with open(path, "rb") as file:
            encrypted_data = file.read()

        decrypted = fernet.decrypt(encrypted_data)

        with open(path, "wb") as file:
            file.write(decrypted)

print("Arquivos restaurados com sucesso.")