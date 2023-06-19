import re

if __name__ == '__main__':
    n = int(input())

    m = 1
    if 1 <= n <= 150:
        lista = [1]
        while m <= (n-1):
            m = m+1
            lista.append(m)
            lista1 = "".join(str(elemento) for elemento in lista)

print(lista1)