import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Configurar el jugador
PLAYER_SIZE = 50
player = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)

# Configurar las teclas de movimiento
LEFT, RIGHT = False, False

def draw_window():
    win.fill((0,0,0))  # Rellenar la ventana de negro
    pygame.draw.rect(win, (255,0,0), player)  # Dibujar al jugador
    pygame.display.update()  # Actualizar la pantalla

def handle_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Mantener al jugador dentro de la ventana
    if player.x < 0:
        player.x = 0
    if player.x > WIDTH - PLAYER_SIZE:
        player.x = WIDTH - PLAYER_SIZE

def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)  # Limitar el juego a 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        handle_movement()
        draw_window()

if __name__ == "__main__":
    main()
