# Diop.io
# Progetto per l'open day del 16 dicembre 2023

# Game developers:
# - Manzoni Thomas
# - Duhanhiu Hegi

# Game artist:
# - Duhanhiu Hegi

import pygame
import sys
from game.gameplay import gest_gameplay

def main():
    while True:
        gest_gameplay()
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()