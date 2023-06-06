a = float(input("insira um número para a ter a sua tabuada: "))
b = int(a)
i = int(1)

def tabuada():
    for i in range(10):
        i = i + 1
        print("{} x {} = {}".format(b, i, b*i))

tabuada()