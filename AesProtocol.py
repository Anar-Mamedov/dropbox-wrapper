#pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import os

class AesProtocol:
    def encryption (key, file_path,output_path,file_name):
        key = str.encode(key)
        cipher = AES.new(key, AES.MODE_CBC)
        file=open(file_path+file_name,'rb').read()
        cipher_text = cipher.encrypt(pad(file, AES.block_size))
        
        with open(output_path+file_name, 'wb') as kfile:
            kfile.write(cipher.iv)
            kfile.write(cipher_text)

    def decryption (key, file_path,output_path,file_name):
        key = str.encode(key)
        with open(file_path+file_name,'rb') as c_text:
            iv = c_text.read(16)
            ct = c_text.read()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        file=open(output_path+file_name,'wb')
        file.write(pt)
        file.close()

AesProtocol.encryption("1F61ECB5ED5D6BAF8D7A7068B28DCC8E","/Users/anarmammadov/Desktop/dropbox_app/", "/Users/anarmammadov/Desktop/","projeno_12.txt")



#AesProtocol.decryption("1F61ECB5ED5D6BAF8D7A7068B28DCC8E","/Users/anarmammadov/Desktop/","/Users/anarmammadov/Desktop/anar/", "projeno_12.txt")
