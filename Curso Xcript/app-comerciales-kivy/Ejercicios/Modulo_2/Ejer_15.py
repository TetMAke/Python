val = input('Digite un caracter: ')
vowels = "aeiou"
a = 0
for vowel in vowels:
    a += 1
    if vowel == val:
        print('Es una vocal')
    elif a == 5:
        print('Es una consonante')
        break
