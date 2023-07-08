from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'This is a 128bit'  # 16 bytes key

file = open("enc_text.txt", "rb")
enc_text = file.read()
file.close()

blocksize = AES.block_size

cipher = AES.new(key, AES.MODE_ECB)
plaintext = b""
for i in range(0, len(enc_text), blocksize):
    block = enc_text[i:i + blocksize]
    if len(block) == blocksize:
        dec_block = cipher.decrypt(block)
        plaintext += dec_block

# Remove the padding from the decrypted plaintext
unpadded_plaintext = unpad(plaintext, blocksize)

print(unpadded_plaintext.decode('utf-8'))
