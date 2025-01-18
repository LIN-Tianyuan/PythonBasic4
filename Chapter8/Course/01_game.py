import pygame
import sys
# Initialiser le pygame
pygame.init()
# Configuration de la fenêtre de l'écran d'accueil
screen = pygame.display.set_mode((400, 400))
screen.fill((135, 206, 235))
# Définir le titre de la fenêtre
pygame.display.set_caption('My first game')
# Introduction des types de polices
f = pygame.font.SysFont('Arial', 50)
# Génère un message texte
"""
Premier paramètre: le contenu du texte
Deuxième paramètre: si la police est lisse ou non
Troisième paramètre: la couleur de la police en mode RGB
Quatrième paramètre: la couleur de fond de la police en mode RGB
"""
text = f.render("Happy game", True, (0, 255, 0), (255, 192, 203))
# Obtenir les coordonnées de la zone rectangulaire de l'objet affiché
textRect = text.get_rect()
# Définir l'objet d'affichage pour qu'il soit centré
textRect.center = (200, 200)
# Prendre le message texte préparé et dessnier sur l'écran d'accueil
screen.blit(text, textRect)


while True:
    # Boucle pour les événements et écoute pour le status de l'événement
    for event in pygame.event.get():
        # Déterminer si l'utilisateur a cliqué sur le bouton de fermeture 'X'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()   # Mise à jour du contenu de l'écran

