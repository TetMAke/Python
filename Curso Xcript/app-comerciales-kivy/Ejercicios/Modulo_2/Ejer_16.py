ip = input('Digite la IP: ')
ind = ip.index('.')
oct = int(ip[:ind])

if 0 <= oct <= 127:
    print("La IP es clase A")
elif 128 <= oct <= 191:
    print("La IP es clase B")
elif 192 <= oct <= 223:
    print("La IP es clase C")
elif 224 <= oct <= 239:
    print("La IP es clase D")
elif 240 <= oct:
    print("La IP es clase E")