import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30 
y = 30
goal_rect = pygame.Rect(200, 200, 60, 60)

while not done:
    player_rect = pygame.Rect(x, y, 60, 60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
            
    if goal_rect.colliderect(player_rect):
        x = 30
        y = 30
    
    pressed = pygame.key.get_pressed() 
    if pressed[pygame.K_UP]: 
        y -= 3 
    if pressed[pygame.K_DOWN]: 
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3 
    if pressed[pygame.K_RIGHT]: 
        x += 3 
    
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, player_rect)
    pygame.draw.rect(screen, (255, 255, 255), goal_rect)
    
    pygame.display.flip()
    clock.tick(60)