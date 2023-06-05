import time

points = 0
points_per_second = 1

# Função para exibir o estado atual do jogo
def display_game_state():
    print(f"Points: {points}")
    print(f"Points per second: {points_per_second}")
    print("")

# Loop principal do jogo
while True:
    display_game_state()
    # Incrementa os pontos com base na taxa de ganho
    points += points_per_second ** 35
    time.sleep(1)  # Aguarda 1 segundo
