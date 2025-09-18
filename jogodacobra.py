import pygame, random, sys
pygame.init()
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
tamanho = 10
x = largura // 2
y = altura //2
vel_x = vel_y = 0
cobra = [[x, y]]
comida = [random.randrange(0, largura - tamanho, tamanho), random.randrange(0, altura - tamanho, tamanho)]
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and vel_y == 0:
                    vel_x = 0; vel_y = -tamanho
            if evento.key == pygame.K_DOWN and vel_y == 0: 
                    vel_x = 0; vel_y = tamanho
            if evento.key == pygame.K_LEFT and vel_x == 0:
                    vel_x = -tamanho; vel_y = 0
            if evento.key == pygame.K_RIGHT and vel_x == 0:
                    vel_x = tamanho; vel_y = 0
    x += vel_x; y += vel_y
    if x < 0 or x >= largura or y < 0 or y >= altura: pygame.quit(); sys.exit()
    cobra.insert(0, [x, y])
    if x == comida[0] and y == comida[1]:
        comida = [random.randrange(0, largura - tamanho, tamanho), random.randrange(0, altura - tamanho, tamanho)]
    else:
        cobra.pop()
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 0, 0), (comida[0], comida [1], tamanho, tamanho))
    for seg in cobra:
        pygame.draw.rect(tela, (0, 255, 0), (seg[0], seg[1], tamanho, tamanho))
    for seg in cobra [1:]:
        if seg == [x, y]: pygame.quit(); sys.exit()
    pygame.display.update()
    relogio.tick(15)