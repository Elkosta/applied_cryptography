#Known values, thanks to the knowledge of the encryption algorithm
A=1103515245
C=12345
n=2**31

#Reading the ciphertext in bytes
f= open("./to_be_decrypted/captured_ct_easy.txt", "rb")
ct=list(f.read())

from_encode = 'From'.encode('ASCII')

#Array with the first ki_b found thanks to the fact that we are aware that the first 4 characters of the plaintext are "From"
ki_b = [a^b for (a,b) in zip(from_encode, ct[0:4])]

print(len(ki_b))
#I rebuild the ki key
ki = ki_b[0]| ki_b[1]<<8|ki_b[2]<<16|ki_b[3]<<24

pt=[]

for i in range(int(len(ct)/4)):
	ki_b = [ki%256, (ki>>8)%256, (ki>>16)%256, (ki>>24)%256]
	pt+=[a^b for (a,b) in zip(ki_b,ct[i*4:i*4+4])]
	ki = (A*ki + C)%n

#Writing the decrypted text to the file "decrypted text.txt"
with open("decrypted text.txt", "wb") as f:
    f.write(bytes(pt))
