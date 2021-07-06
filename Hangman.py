import math
import pygame
import random
import os
from words import new_words

# Setup display

pygame.init()
WIDTH, HEIGHT = 1200, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# Loading images

os.chdir("C:/Users/Jonathan Challenger/PycharmProjects/PythonProjects/images")
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    image = pygame.transform.scale(image, (270, 280))
    images.append(image)

# Button variables
RADIUS = 30
GAP = 20
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 525

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 50)
WORD_FONT = pygame.font.SysFont('comicsans', 80)
TITLE_FONT = pygame.font.SysFont('comicsans', 100)

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Setup game loop


def draw():
    win.fill(WHITE)

    text = TITLE_FONT.render("HANGMAN", True, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, True, BLACK)
    win.blit(text, (425, 300))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (125, 125))
    pygame.display.update()


def draw_button(screen, position, text):
    text_render = WORD_FONT.render(text, True, WHITE)
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.rect(screen, BLACK, (x, y, w, h))
    return screen.blit(text_render, (x, y))


def display_message(message1, message2):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text1 = WORD_FONT.render(message1, True, BLACK)
    text2 = WORD_FONT.render(message2, True, BLACK)
    win.blit(text1, ((WIDTH / 2 - text1.get_width() / 2), (HEIGHT / 2 - text1.get_height() / 2 - 50)))
    win.blit(text2, ((WIDTH / 2 - text2.get_width() / 2), (HEIGHT / 2 - text2.get_height() / 2 + 50)))
    pygame.display.update()
    pygame.time.delay(3000)


def letter_list():
    A = 65
    let_list = []
    for let in range(26):
        x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (let % 13)
        y = starty + ((let // 13) * (GAP + RADIUS * 2))
        let_list.append([x, y, chr(A + let), True])
    return let_list


def main():
    global hangman_status, word, guessed, letters
    hangman_status = 0
    word = random.choice(new_words).upper()
    guessed = []

    letters = letter_list()

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You WON!", f"The word was {word}")
            run = False
            guessed = []

        if hangman_status == 6:
            display_message("You LOST!", f"The word was {word}")
            run = False
            guessed = []


def main_menu(window):
    run = True
    while run:
        window.fill(WHITE)
        b1 = draw_button(window, (WIDTH / 2 - 100, 200), "PLAY")
        b2 = draw_button(window, (WIDTH / 2 - 100, 400), "QUIT")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    main()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    run = False
        pygame.display.update()
    pygame.display.quit()


main_menu(win)
pygame.quit()
