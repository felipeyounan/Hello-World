l = float(input("Qual é a largura da parede (em metros) que você deseja pintar? "))
h = float(input("Qual é a altura (em metros) dessa mesma parede?"))
re = float(input("Qual é a superfície de recobrimento(m²/L) da tinta? "))

at = (l*h)/re
print("Para uma parede de {}m² você vai precisar de {}L de tinta".format(l*h, at))

