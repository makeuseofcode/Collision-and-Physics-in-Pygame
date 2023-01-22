import pygame

# Global constants
GRAVITY = 0.5
JUMP_VELOCITY = -10
FRICTION = 0.9
ACCELERATION = 0.5

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):
        self.rect.y += self.y_velocity
        self.rect.x += self.x_velocity
        self.y_velocity += GRAVITY
        self.x_velocity *= FRICTION

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Create player and platform sprites
player = Player(100, 300)
player_group = pygame.sprite.Group()
player_group.add(player)

platform = Platform(50, 400, 100, 20)
platform_group = pygame.sprite.Group()
platform_group.add(platform)

player_movement = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.y_velocity = JUMP_VELOCITY
            elif event.key == pygame.K_LEFT:
                player_movement = -1
            elif event.key == pygame.K_RIGHT:
                player_movement = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_movement = 0
                
    player.x_velocity += player_movement * ACCELERATION
    player_group.update()
    collided_sprites = pygame.sprite.spritecollide(player, platform_group, False)
    screen.fill((255, 255, 255))
    player_group.draw(screen)
    platform_group.draw(screen)

    if collided_sprites:
        player.y_velocity = 0
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render('Collision: True', False, (0, 0, 0))
        screen.blit(text, (320, 240))
    pygame.display.flip()

pygame.quit()
