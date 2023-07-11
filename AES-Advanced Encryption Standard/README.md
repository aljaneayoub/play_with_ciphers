# AES Encryption and Decryption

This script provides a command-line interface for AES encryption and decryption using the ECB mode. AES (Advanced Encryption Standard) is a symmetric encryption algorithm widely used for secure data transmission and storage.

## Requirements

- Python 3.x
- pycryptodome library (can be installed via `pip install pycryptodome`)

## Usage

### Encryption

To encrypt a plaintext, use the `-e` or `--encode` flag along with the plaintext input. You can provide the input either as a text or a file.

Text input:

      $ python enc_dec_AES.py -e -m ECB -t "This is my plaintext"

File input:

      $ python enc_dec_AES.py -e -m ECB -f plaintext.txt


### Decryption

To decrypt a ciphertext, use the `-d` or `--decode` flag along with the ciphertext input. Again, you can provide the input as text or a file.

Text input:

      $ python enc_dec_AES.py -d -m ECB -t "\x16\xd8\x1f?\x0ea\xc7m0\xa8\x00\xb8\x86\x02\x8cO\xa8\t\xeb\xda\x82\xb2\xfb\xabw\xae1\xe2\xf0I\xe96\xf3L\xbb\x8d0\x8d\x93\xd4?\xfd\x14\xd6\x04\xc6P\xf9\x03d\x86}\xfa\xe4S\t\xea\x84F\xa0\xde\xc1kO#\xe3\x9af\xb6\xe5|\x9b^\xcdf-\xe2*\x10\xcc"


File input:

      $ python enc_dec_AES.py -d -m ECB -f ciphertext.txt


**Note:** Ensure that you choose the correct mode (`-m`) when encrypting and decrypting.

## Limitations

- This script currently supports only the ECB mode of AES.
- Padding is applied to the plaintext before encryption, and unpadding is performed during decryption. Ensure that the plaintext is padded correctly.

Feel free to modify and enhance the script according to your specific requirements. Enjoy encrypting and decrypting with AES!
