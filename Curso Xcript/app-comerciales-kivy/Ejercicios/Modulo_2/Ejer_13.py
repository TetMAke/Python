num = []
for i in range(3):
    num.append(int(input("Digite el número: ")))

may = 0
for i in range(len(num)):
    if num[i] >= may:
        may = num[i]

print(f"Número mayor es: {may}")