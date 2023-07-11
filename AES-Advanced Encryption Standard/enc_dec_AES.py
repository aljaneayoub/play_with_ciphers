import argparse
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import random





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encode", help="Use for encoding plaintext", action='store_true')
    parser.add_argument("-d", "--decode", help="Use for decoding ciphertext", action='store_true')
    parser.add_argument("-m", "--mode", help="Specify AES mode", type=str.upper)
    parser.add_argument("-t", "--text", help="Input text", type=str)
    parser.add_argument("-f", "--file", help="Input file", type=argparse.FileType('r'))
    args = parser.parse_args()

    if args.text:
        plaintext=args.text
        plaintext=plaintext.encode("utf-8")


        key=b"This is a 128bit" # 16 bytes key

        #key=get_random_bytes(16) # random 16 bytes key

        #key = b'this is a 192bits secret' # 24 bytes key

        #key = b'this is a 256bits secret key !!!' # 32 bytes key


        blocksize=AES.block_size
        padded_plaintext=pad(plaintext,blocksize)
    elif args.file:
        file=args.file
        plaintext=file.read()
        plaintext=plaintext.encode("utf-8")
        key=b"This is a 128bit" # 16 bytes key
        blocksize=AES.block_size
        padded_plaintext=pad(plaintext,blocksize)
    else: 
        print("you need to choose the input between file '-f' or text '-t' ")

    if args.mode:
        key=b"This is a 128bit"
        if args.mode == 'ECB':
            cipher_ECB=AES.new(key,AES.MODE_ECB)


        else:
            print("you need to choose between ECB or CBC")
    else:
        print("you need to use mode argument 'm'")

    if args.encode:
        cipher_enc=b""
        try:
            blocks=[padded_plaintext[i:i+blocksize]for i in range(0,len(padded_plaintext),blocksize)]
        
            for block in blocks:
                if args.mode == "ECB":
                    enc_block=cipher_ECB.encrypt(block)

                cipher_enc+=enc_block
        
            formatted_ciphertext = repr(cipher_enc)[2:-1]
            print(formatted_ciphertext)
        except UnboundLocalError:
            print("you need to choose -m and the mode ECB to decrypte the block") 

    if args.decode:
        if args.file:
            ciphertext=plaintext
            ciphertext = ciphertext.decode('unicode_escape').encode('latin-1')


        elif args.text:
            ciphertext = args.text.encode("utf-8")
            ciphertext = ciphertext.decode('unicode_escape').encode('latin-1')

        else:
            print("You need to provide the ciphertext either through a file or as text input")

        blocksize = AES.block_size
        deciphertext = b''
        try:
            for i in range(0,len(ciphertext),blocksize):
                block=ciphertext[i:i+blocksize]
                
                dec_block=cipher_ECB.decrypt(block)
                
                deciphertext+=dec_block


            unpadding_plaintext=unpad(deciphertext,blocksize)
            print(unpadding_plaintext.decode("utf-8"))
        except UnboundLocalError:
                print("you need to choose -m and the mode ECB to decrypte the block")
if __name__ == '__main__':
    main()
