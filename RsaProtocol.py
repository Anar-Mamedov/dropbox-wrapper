#pip install pycryptodome 
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP



class RsaProtocol:
    def create_key(self):
        key = RSA.generate(2048)
        private_key = key.exportKey()
        with open("./private.pem", "wb") as f:
            f.write(private_key)

        public_key = key.publickey().exportKey()
        with open("public.pem", "wb") as f:
            f.write(public_key)
    #key_path='c:/.../public.pem'
    #output_path='c:/.../'
    def encryption(self,key_path,output_path,data_text):
        data = data_text.encode("utf-8")
        with open(output_path+"crypted_key.bin", "wb") as f:
        
            recipient_key = RSA.import_key(open(key_path).read())
            session_key = get_random_bytes(16)
        
            # Encrypt the session key with the public RSA key
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)
        
            # Encrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            [ f.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    #key_path='c:/.../private.pem'
    #data_path='c:/.../crypted_key.bin'
    def decryption(self, key_path, data_path):
        with open(data_path, "rb") as f:

            private_key = RSA.import_key(open(key_path).read())
        
            enc_session_key, nonce, tag, ciphertext = \
               [ f.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
        
            # Decrypt the session key with the private RSA key
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)
        
            # Decrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            return data.decode("utf-8")             