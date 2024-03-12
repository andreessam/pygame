import pygame
from pygame.locals import *

# Classe pour gérer la fenêtre et les événements
class App:
    def __init__(self):
        pygame.init()

        # Définition des dimensions de la fenêtre
        self.window_width = 600
        self.window_height = 600

        # Création de la fenêtre graphique
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Affichage des codes et touches clavier")

        # Définition de la police d'écriture
        self.font = pygame.font.Font(None, 36)

        # Liste pour stocker les codes et les touches
        self.key_list = []

        # Variables pour la gestion du défilement
        self.scroll_position = 0
        self.scroll_speed = 40  # Vitesse de défilement en pixels par pression de touche

    def run(self):
        # Boucle principale de l'application
        running = True
        while running:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        # Défilement vers le haut lors de la pression de la touche flèche haut
                        self.scroll_position -= self.scroll_speed
                    elif event.key == K_DOWN:
                        # Défilement vers le bas lors de la pression de la touche flèche bas
                        self.scroll_position += self.scroll_speed

                    # Récupération du code et de la touche pressée
                    key_code = event.key
                    key_name = pygame.key.name(key_code)

                    # Ajout du code et de la touche à la liste
                    self.key_list.append(f"Code: {key_code}   Touche: {key_name}")

                    # Limitation de la liste à 15 éléments pour éviter un affichage trop long
                    self.key_list = self.key_list[-15:]

                    # Mise à jour de la position de défilement pour afficher la dernière ligne ajoutée
                    self.scroll_position = max(0, len(self.key_list) * 40 - self.window_height)

            self.update()
            self.render()

        self.quit()

    def update(self):
        pass

    def render(self):
        # Effacement de la fenêtre
        self.window.fill((187, 210, 225))

        # Création d'une surface plus grande que la fenêtre visible
        surface = pygame.Surface((self.window_width, len(self.key_list) * 40))
        surface.fill((187, 210, 225))

        # Affichage des codes et des touches sur la surface
        for i, key_text in enumerate(self.key_list):
            text_surface = self.font.render(key_text, True, (5, 5, 5))
            surface.blit(text_surface, (10, i * 40))

        # Affichage de la portion de la surface correspondant à la fenêtre visible
        self.window.blit(surface, (0, -self.scroll_position))

        # Rafraîchissement de la fenêtre
        pygame.display.flip()

    def quit(self):
        # Fermeture de pygame
        pygame.quit()

# Création de l'application et exécution
app = App()
app.run()
# Fermeture de pygame
pygame.quit()