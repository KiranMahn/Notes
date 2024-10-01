
## Encrypt plain.txt into encrypted.txt 

openssl enc -aes-256-cbc -pbkdf2 -a -in /Users/kiranmahn/notes/cs407/1-13/plain.txt -out /Users/kiranmahn/notes/cs407/1-13/encrypted.txt

## Decrypt encrypted.txt using password set in first step into decryptedfile.txt

openssl enc -aes-256-cbc -d -pbkdf2 -a -in /Users/kiranmahn/notes/cs407/1-13/encrypted.txt -out /Users/kiranmahn/notes/cs407/1-13/decryptedfile.txt


-d specifies decryption mode, and -pbkdf2 ensures the key derivation matches the encryption process. The decrypted content will be written to decryptedfile.txt at the specified path.

-in indicates that the next token contains the name of the file to be decrypted

-a instructs OpenSSL to encode the result in Base64, meaning the encrypted output will be human-readable and can be opened in a text editor.

-out specifies that the next token is the name of the file to be written, which will be the encrypted version.


