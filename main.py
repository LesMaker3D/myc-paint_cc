import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
done = True
draw = False
screen.fill((255, 255, 255))
taille = 6
lignecolor = 0, 0, 0
while done:
    for event in pygame.event.get():
        pygame.draw.circle(screen, lignecolor, (15, 15), 10)
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = False
        elif event.type == pygame.MOUSEMOTION:
            if draw:
                pygame.draw.circle(screen, lignecolor, pygame.mouse.get_pos(), taille)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        elif event.type == pygame.MOUSEBUTTONUP:
            draw = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                lignecolor = (255, 0, 0)
            if event.key == pygame.K_g:
                lignecolor = (0, 255, 0)
            if event.key == pygame.K_b:
                lignecolor = (0, 0, 255)
            if event.key == pygame.K_j:
                lignecolor = (255, 255, 0)
            if event.key == pygame.K_c:
                lignecolor = (0, 255, 255)
            if event.key == pygame.K_n:
                lignecolor = (255, 0, 255)
            if event.key == pygame.K_f:
                screen.fill(lignecolor)
            if event.key == pygame.K_1:
                taille = 1
            if event.key == pygame.K_2:
                taille = 2
            if event.key == pygame.K_3:
                taille = 3
            if event.key == pygame.K_4:
                taille = 4
            if event.key == pygame.K_5:
                taille = 5
            if event.key == pygame.K_6:
                taille = 6
            if event.key == pygame.K_7:
                taille = 7
            if event.key == pygame.K_8:
                taille = 8
            if event.key == pygame.K_9:
                taille = 9
            if event.key == pygame.K_s:
                nameFile = input('Inserez un nom de fichier: ')
                pygame.image.save(screen, nameFile+'.png')
    pygame.display.flip()

pygame.quit()
