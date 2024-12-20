import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
white=(255,255,255)
screen.fill(white)

pygame.display.update()

candy_crush = pygame.image.load("candycrush.png")
ludo = pygame.image.load("ludo.png")
subway_surfers= pygame.image.load("subwaysurfers.png")
temple_rush = pygame.image.load("templerush.png")

screen.blit(subway_surfers, (150,100))
screen.blit(ludo, (150,200))
screen.blit(temple_rush, (150,300))
screen.blit(candy_crush, (150,400))

font = pygame.font.SysFont("Georgia", 20)

text1 = font.render("Ludo", True, (0,0,0))
text2 = font.render("Candy crush", True, (0,0,0))
text3 = font.render("Subway Surfers", True, (0,0,0))
text4 = font.render("Temple rush", True, (0,0,0))

screen.blit(text1, (350,100))
screen.blit(text2, (350,200))
screen.blit(text3, (350,300))
screen.blit(text4, (350,400))

pygame.display.update()

while True:
    event = pygame.event.poll()