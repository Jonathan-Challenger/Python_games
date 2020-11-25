import pygame
import random 
import tkinter as tk
from tkinter import messagebox
import sys

def draw_floor():
	screen.blit(floor, (floor_x_pos, 500))
	screen.blit(floor, (floor_x_pos + 360, 500))

pygame.init()
pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((360, 640))
clock = pygame.time.Clock()

bg = pygame.image.load('flappy_background.png')

floor = pygame.image.load('base.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(bg,(0,0))
	floor_x_pos -= 2
	draw_floor()
	if floor_x_pos <= -360:
		floor_x_pos = 0

	pygame.display.update()
	clock.tick(60)