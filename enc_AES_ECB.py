from Crypto.Cipher import AES
#from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad ,unpad


# ECB (Electronic Codebook):

#     Not recommended for most applications due to its vulnerability to certain attacks.
#     Can be used in specific cases where unique blocks of data are guaranteed.


file = open("plaintext.txt","+r")
text=file.read()
file.close()

plaintext = text.encode("utf-8")



#encryption key size can be 128, 192 or 256 bits

#key=get_random_bytes(16) # random 16 bytes key
key = b'This is a 128bit'  # 16 bytes key
#key = b'this is a 192bits secret' # 24 bytes key
#key = b'this is a 256bits secret key !!!' # 32 bytes key

cipher=AES.new(key,AES.MODE_ECB)

blocksize=AES.block_size #block size : 16 bytes

padding_text=pad(plaintext,blocksize)


blocks=[padding_text[i:i+blocksize] for i in range(0,len(padding_text),blocksize)]

enc_text=b""
for block in blocks:
    enc_block=cipher.encrypt(block)
    enc_text+=enc_block
    
print(enc_text)
text=enc_text.replace("\\",)

deciphertext = b''
for i in range(0,len(enc_text),blocksize):
    block=enc_text[i:i+blocksize]
    dec_block=cipher.decrypt(block)
    deciphertext+=dec_block


unpadding_plaintext=unpad(deciphertext,blocksize)
print(unpadding_plaintext)
