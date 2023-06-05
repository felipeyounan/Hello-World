

c=input("insira um  novo pais: ")
d=input("insira a capital do pais inserido: ")
a=input(str("Insina o nome do pais: "))

capitais = {"USA":"Washington, DC",
            "India":"Nova Deli",
            "China":"Pequin",
            "Russia":"Moscou"}
capitais[c]=d

print(f"A capital de", a, " é ", capitais.get(a))