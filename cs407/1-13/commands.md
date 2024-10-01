
## Encrypt plain.txt into encrypted.txt 

openssl enc -aes-256-cbc -pbkdf2 -a -in /Users/kiranmahn/notes/cs407/1-13/plain.txt -out /Users/kiranmahn/notes/cs407/1-13/encrypted.txt

## Decrypt encrypted.txt using password set in first step into decryptedfile.txt

openssl enc -aes-256-cbc -d -pbkdf2 -a -in /Users/kiranmahn/notes/cs407/1-13/encrypted.txt -out /Users/kiranmahn/notes/cs407/1-13/decryptedfile.txt

