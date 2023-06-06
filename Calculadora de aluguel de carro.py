lista = {
    "Verona" : 110.00,
    "Cadete" : 110.00,
    "Monza" : 150.00,
    "Camaro" : 25.00
}
escolha = input(f"Bem vindo a locadora do Seu Antão!\n"
      "Temos apenas belos exemplares para alugar! Quanto melhor o carro, mais caro! \n"
      "Qual destestes belos exemplares voê gostaria de alugar?!"
      f"{list(lista.keys())}")

carro = lista.get(escolha)
dist = int(input("Quantos quilometros você rodou com o carro?"))
tempo = int(input("Qauntos dias você ficou com o carro?"))


print(f"Para o", escolha, "que tem um alugue ldiário de R$ ",carro,
      "você teve uma despesa de total de: R$",((dist*0.15)+(carro*tempo))

      )




