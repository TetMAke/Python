num = []
for i in range(int(input("Cuantos numeros va a digitar: "))):
    num.append(int(input(f"Digite el número {i}: ")))

may = 0
men = 10000000000000000
for i in range(len(num)):
    for j in range(len(num)-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1],num[j]

print(f"Los numeros ordenados son: {num}")