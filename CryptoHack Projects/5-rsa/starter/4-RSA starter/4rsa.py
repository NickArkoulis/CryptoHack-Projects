from CryptoLib import modinv
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
tot = ( (p-1) * (q-1) )
 x = modinv(65537, tot)
 print(x)
