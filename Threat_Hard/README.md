# Thread_easy
The purpose of this exercise is to implement an algorithm that is able to decrypt the file located in the **to_be_decrypted** folder. In order to decrypt we are aware of the encryption algorithm used **perfect_cipher_generator_easy.py**.
********************************

The encryption algorithm is based on LCG ([Linear Congruential Generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) ) to generate a different encryption key for each byte of the plaintext. In this case LCG is very simple. The strength of the encryption algorithm lies in the fact that A and C (values ​​used by LCG) are chosen randomly in a very large space.

 However, taking advantage of the fact that each message begins with the string "From:" and an important property of modular algebra, it is possible to drastically reduce the search space of the two values ​​A and C.

 
The property of the modular algebra used is:

    A*ki + C mod n = ((A mod n) * ki + (C mod n)) mod n

Taking advantage of the previous property, it is possible to reduce the search space of the values ​​A and C in the following way:

    A = A mod n
    C = C mod n


The search space of A and C was reduced in the range of values ​​(0,255)