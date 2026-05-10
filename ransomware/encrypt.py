from cryptography.fernet import Fernet
import os

# Gera chave
key = Fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

folder = "test_files"

# Verifica pasta (Caso não exista, criar e encerrar para o usuário colocar os arquivos)
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Pasta '{folder}' criada.")
    print("Adicione os arquivos para serem criptografados.")
    exit()

files = os.listdir(folder)

print("Arquivos encontrados:", files)

for filename in files:

    path = os.path.join(folder, filename)

    if os.path.isfile(path):

        print(f"Criptografando: {filename}")

        with open(path, "rb") as file:
            original_data = file.read()

        encrypted_data = fernet.encrypt(original_data)

        with open(path, "wb") as file:
            file.write(encrypted_data)

print("Concluído.")