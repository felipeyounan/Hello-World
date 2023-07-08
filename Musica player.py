import pygame

musica = "naise nina oliveira cove [vocals].mp3"

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
pygame.event.wait()

print(f"tocando nesse momento", musica)
