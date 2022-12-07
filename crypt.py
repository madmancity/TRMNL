# LCR
# Encryption and Decryption functions
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
# Import private key from user's system
with open("C:\\Program Files\\UTPRQ-LGA\\UTPRQ-QT.key", "rb") as key_file:
        # Serialize .pem format
        privatekey = serialization.load_pem_private_key(
            # Read file to privatekey
             key_file.read(),
            # Password could be added later, but I read that it generally causes more problems than it fixes
            password=None,
        )

# Encrypt message
def encrypt(message):
    # Generate public key
    public_key = privatekey.public_key()
    # Encrypt
    ciphertext = public_key.encrypt(
        message,
        # Using OAEP padding, as its more compatible with rsa encryption
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Write ciphertext to text file in encryption folder
    cptfile = open("C:\\Program Files\\UTPRQ-LGA\\drw.txt", "w")
    cptfile.write(str(ciphertext))
    cptfile.close()
    return ciphertext

# Decryption function
def decrypt(ciphertext):
    # Decrypt ciphertext using privatekey
    plaintext = privatekey.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Convert plaintext to string
    ptxt = plaintext.decode()
    return ptxt

