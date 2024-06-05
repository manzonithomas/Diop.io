import pygame
import sys
from game.impostazioni import NERO, BIANCO

def mostra_schermata_sconfitta(schermo, larghezza_schermo, altezza_schermo, clock, FPS):
    jumpscare_sound = pygame.mixer.Sound("img/suono_jump.mp3")
    jumpscare_image = pygame.image.load("img/imm_jump.jpg")
    jumpscare_image = pygame.transform.scale(jumpscare_image, (larghezza_schermo, altezza_schermo))
        
    while True:
            jumpscare_sound.play()
            schermo.blit(jumpscare_image, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2000)
            break
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        sfondo_game_over = pygame.image.load("img/gameover.jpg")
        sfondo_game_over = pygame.transform.scale(sfondo_game_over, (larghezza_schermo, altezza_schermo))
        schermo.blit(sfondo_game_over, (0, 0))

        # "Riprova"
        pulsante_menu = pygame.Rect(larghezza_schermo - 400, 500, 200, 50)
        pygame.draw.rect(schermo, BIANCO, pulsante_menu)

        font_pulsante = pygame.font.Font(None, 36)
        testo_pulsante = font_pulsante.render("Riprova", True, (0, 0, 0))
        schermo.blit(testo_pulsante, (larghezza_schermo - 300 - testo_pulsante.get_width() // 2, 515))

        # "Chiudi Gioco"
        pulsante_chiudi = pygame.Rect(larghezza_schermo - 400, 600, 200, 50)
        pygame.draw.rect(schermo, BIANCO, pulsante_chiudi)

        testo_chiudi = font_pulsante.render("Chiudi Gioco", True, (0, 0, 0))
        schermo.blit(testo_chiudi, (larghezza_schermo - 300 - testo_chiudi.get_width() // 2, 615))
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # tornare al menu e chiduere il gioco
        if pulsante_menu.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            return True

        if pulsante_chiudi.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(FPS)
