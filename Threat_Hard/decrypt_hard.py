#Reading the ciphertext in bytes
f= open("./ciphertext.txt", "rb")
ct=list(f.read())

#The value of n is specified in the encryption algorithm
n=256


finalA = -1
finalC = -1

from_encode = 'From'.encode('ASCII')
know_ki_from = [a^b for (a,b) in zip(from_encode, ct[0:4])]

#The breaking of the cipher depends on how easy it is to calculate the A and C values ​​used. 
#In our case it is possible to drastically reduce the search space by exploiting a property 
#of modular algebra and knowing that all encrypted messages begin with the string "From:"
for A in range(0,256):
    for C in range(0,255):
        check_k1 = ((A * know_ki_from[0]) + C) % n
        check_k2  = ((A * know_ki_from[1]) + C) % n
        check_k3  = ((A * know_ki_from[2]) + C) % n
        if(check_k1 == know_ki_from[1] and check_k2 == know_ki_from[2] and check_k3 == know_ki_from[3]):
            finalA = A
            finalC = C
            break
        
if(finalA == -1 and finalC == -1):
    print("Values ​​of A and C were not found")
    exit()

decripted_text = []

ki = know_ki_from[0] 

#Calculating the original message by making the exclusive or between the key and the ciphertext
for i in range(len(ct)-1):
    decripted_text.append(ki ^ ct[i])
    ki = ((finalA*ki) + finalC) % n 

#Writing the decrypted text to the file "decrypted text.txt"
with open("decrypted_text.txt", "wb") as f:
    f.write(bytes(decripted_text))