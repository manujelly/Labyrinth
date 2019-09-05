import pygame
#import Labyrinth
import Board
import Player


pygame.init()

window = pygame.display.set_mode((600, 600))

display = 1



a = Board.Board()
data = a.initialBoard()
color = (255, 255, 255)
red=(255,0,0)

position=[]

while display:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        else:

            for i in range(len(data)):
                  for j in range(len(data[0])):
                    to_x=1+(i*50)
                    to_y=1+(j*50)
                    position.append([to_x,to_y])
                    if data[i][j]==1:
                        pygame.draw.rect(window,red,(to_x,to_y,50,50))
                    elif data[i][j]==0:
                        pygame.draw.rect(window,color,(to_x,to_y,50,50),3)
                    elif data[i][j]==3:
                        pygame.draw.rect(window,color,(to_x,to_y,50,50),1)



    pygame.display.flip()
