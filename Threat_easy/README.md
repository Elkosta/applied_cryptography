# Thread_easy
The purpose of this exercise is to implement an algorithm that is able to decrypt the file located in the **to_be_decrypted** folder. In order to decrypt we are aware of the encryption algorithm used **perfect_cipher_generator_easy.py**.
********************************

The encryption algorithm is based on LCG ([Linear Congruential Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) )  to generate different encryption keys for each block. In this case LCG is very simple. Moreover, thanks to the knowledge that **each message to be encrypted must start with the string "From:"**, implementing a decryption algorithm is very simple.
