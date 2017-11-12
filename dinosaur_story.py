import sys, pygame
from pygame.locals import *

#main program
pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption("Dino Trivia Quiz")
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)
white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0
black = 0,0,0

def print_text(font, x, y, text, colour=(255,255,255), shadow=False):
    if shadow:
        imgText = font.render(text, True, (0,0,0))
        screen.blit(imgText, (x-2,y-2))
    imgText = font.render(text, True, colour)
    screen.blit(imgText, (x,y))


#repeating loop
while True:

    #clear the screen
    screen.fill((0,0,200))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    #show dino story
    print_text(font1, 210, 5, "The Dino Story", black)
    print_text(font2,20, 80, "Trooden was the smartest, brainiest, most inteligent dinosaur of them all. His brain was similar in size", red)
    print_text(font2, 20, 110, "to a present-day mammal. This was something he always liked to remind his fellow dino-companions of.", red)
    print_text(font2, 20, 140, "The Mapusaurus roseae (Map), however had grown tired of Troodens constant bragging, so they banded together,", red)
    print_text(font2, 20, 170, "forming a pack, with the intent of hunting down the highly inteligent Trooden.", red)
    print_text(font2, 20, 200, "So, one day, while Trooden was informing Anthony, the Argentinosaurus, that the smallest dinosaur egg", red)
    print_text(font2, 20, 230, "was only a measly 30cm in length (the length of the average ruler), and being a mightly 77 tonnes", red)
    print_text(font2, 20, 260, "Anthony should stay well clear of these small eggs, unless he wished to crush them under his mighty", red)
    print_text(font2, 20, 290, "feet. The Map pack crept up, and attempted to surround Trooden.", red)
    print_text(font2, 20, 320, "However, Trooden, being so intelligent, was aware of his unpopularity, making him always on the lookout", red)
    print_text(font2, 20, 350, "for predators.  He spotted the pack coming and quickly scarpered.", red)
    print_text(font2, 20, 380, "He knew that the Map pack could not swim, and so headed for water. Finding a crossing by passing over a", red)
    print_text(font2, 20, 410, "fallen tree, he headed to an island in the middle of a river, and quickly pushed the tree into the river", red)
    print_text(font2, 20, 440, "so it no longer formed a bridge.", red)
    print_text(font2, 20, 470, "The Map pack were dissuaded from their pursuit by the sight of the water, however, another dinosaur had",red)
    print_text(font2, 20, 500, "been watching the chase, and he also to did not like Trooden. Spiny the Spinosaurus aegyptiacus was perhaps", red)
    print_text(font2, 20, 530, "the largest carnivore to ever live, measuring 50 feet long. This, however, was not what made him so deadly.",red)
    print_text(font2, 20, 560, "No, it was the fact that, unlike most dinosaurs, Spiny could swim!", red)
    print_text(font2, 20, 590, "Dun Dun Dun...", red)
    #dino askii
    print_text(font2, 80, 590, "                          __", white)
    print_text(font2, 80, 610, "                        /  _  )", white)
    print_text(font2, 80, 630, "        _.-------._/  /", white)
    print_text(font2, 80, 650, "       /                 /", white)
    print_text(font2, 80, 670, " __/   (   |   (    |", white)
    print_text(font2, 80, 690, "/__.-'  |_| --| _|", white)
    
    #update display
    pygame.display.update()
