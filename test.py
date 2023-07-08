import argparse
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad

plaintext=b"hello my name is ayoub aljane"


key=b"This is a 128bit" # 16 bytes key

#key=get_random_bytes(16) # random 16 bytes key

#key = b'this is a 192bits secret' # 24 bytes key

#key = b'this is a 256bits secret key !!!' # 32 bytes key



blocksize=AES.block_size
padded_plaintext=pad(plaintext,blocksize)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encode", help="Use for encoding plaintext", action='store_true')
    parser.add_argument("-d", "--decode", help="Use for decoding ciphertext", action='store_true')
    parser.add_argument("-m", "--mode", help="Specify AES mode", type=str.upper)
    parser.add_argument("-t", "--text", help="Input text", type=str)
    parser.add_argument("-f", "--file", help="Input file", type=argparse.FileType('r'))
    args = parser.parse_args()

    if args.mode:
        if args.mode == 'ECB':
            cipher_ECB=AES.new(key,AES.MODE_ECB)

        elif args.mode == "CBC":
            cipher_CBC=AES.new(key,AES.MODE_CBC)
        else:
            print("you need to choose between ECB or CBC")


    if args.encode:
        cipher_enc=b""
        blocks=[padded_plaintext[i:i+blocksize]for i in range(0,len(padded_plaintext),blocksize)]
        for block in blocks:
            enc_block=cipher_ECB.encrypt(block)
            cipher_enc+=enc_block
        print(f"encrypted text : {cipher_enc}")

        
    if args.decode:
        print("The parameter is decoding")


    if args.text:
        print("The input text is:", args.text)


    if args.file:
        print("The input file is:", args.file)

if __name__ == '__main__':
    main()
