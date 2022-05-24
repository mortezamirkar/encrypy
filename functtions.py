from cryptography.fernet import Fernet
def createKeyFike():
    key=Fernet.generate_key()
    with open("key.key","wb") as keyfile:
        keyfile.write(key)
def encrypt(filename,keyfile):
    with open(filename,"rb") as file:
        file_data=file.read()
    with open(keyfile,"rb") as keyfiles:
        key=keyfiles.read()
    encrypted_data=Fernet(key).encrypt(file_data)
    with open(filename,"wb") as file:
        file.write(encrypted_data)

def decrypt(filename,keyfile):
    with open(keyfile,"rb") as keyfile:
        key=keyfile.read()
    with open(filename,"rb") as file:
        encrypted_data=file.read()
    file_data=Fernet(key).decrypt(encrypted_data)
    with open(filename,"wb") as file:
        file.write(file_data)