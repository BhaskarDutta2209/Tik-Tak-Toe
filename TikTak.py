import pygame
import time
from random import *
import sys
from pygame import mixer

pygame.init()
pygame.font.init()

sign = None
csign = None

board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

white = (255,255,255)
orange = (245, 102, 0)
black = (0,0,0)
purple = (82, 45, 128)
orange = (245, 102, 0)

#Background
clemson = pygame.image.load('images/Clemson.png')

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tik Tak Toe")

gameDisplay.fill(white)
gameDisplay.blit(clemson, (225, 450))

# Sound
mixer.music.load("TikTakmusic.mp3")
mixer.music.play(-1)


def drawBoard():
    gameDisplay.fill(white)
    gameDisplay.blit(clemson, (225,450))

    #The code below draws the matrix board
    
    pygame.draw.line(gameDisplay,orange,(display_width//2 - 50,display_height//2 - 150),(display_width//2 - 50,display_height//2 + 150),4)
    pygame.draw.line(gameDisplay,orange,(display_width//2 + 50,display_height//2 - 150),(display_width//2 + 50,display_height//2 + 150),4)
    pygame.draw.line(gameDisplay,orange,(display_width//2 - 150,display_height//2 - 50),(display_width//2 + 150,display_height//2 - 50),4)
    pygame.draw.line(gameDisplay,orange,(display_width//2 - 150,display_height//2 + 50),(display_width//2 + 150,display_height//2 + 50),4)

def drawCross(x,y):
    pygame.draw.line(gameDisplay,purple,(x+10,y+10),(x+90,y+90),6)
    pygame.draw.line(gameDisplay,purple,(x+90,y+10),(x+10,y+90),6)
    
def drawCircle(x,y):
    pygame.draw.circle(gameDisplay,orange,(x+50,y+50),45,6)




def getStartingPoint(box):
    if box==(0,0):
        return (display_width//2-150,display_height//2-150)
    elif box==(0,1):
        return (display_width//2-50,display_height//2-150)
    elif box==(0,2):
        return (display_width//2+50,display_height//2-150)
    elif box==(1,0):
        return (display_width//2-150,display_height//2-50)
    elif box==(1,1):
        return (display_width//2-50,display_height//2-50)
    elif box==(1,2):
        return (display_width//2+50,display_height//2-50)
    elif box==(2,0):
        return (display_width//2-150,display_height//2+50)
    elif box==(2,1):
        return (display_width//2-50,display_height//2+50)
    elif box==(2,2):
        return (display_width//2+50,display_height//2+50)
        

def boxLocation(mousePos):
    x = mousePos[0]
    y = mousePos[1]
    if x <= (display_width//2-50) and x > (display_width//2 - 150):

        if y>(display_height//2 - 150) and y <= (display_height//2 - 50):
            return (0,0)
        if y>(display_height//2 - 50) and y <= (display_height//2+50):
            return (1,0)
        if y>(display_height//2 + 50) and y <= (display_height//2+150):
            return (2,0)

    if x <= (display_width//2+50) and x > (display_width//2-50):
        if y>(display_height//2-150) and y <= (display_height//2-50):
            return (0,1)
        if y>(display_height//2-50) and y <= (display_height//2+50):
            return (1,1)
        if y>(display_height//2+50) and y <= (display_height//2+150):
            return (2,1)
        
    if x <= (display_width//2+150) and x > (display_width//2+50):
        if y>(display_height//2-150) and y<=(display_height//2-50):
            return (0,2)
        if y>(display_height//2-50) and y<=(display_height//2+50):
            return (1,2)
        if y>(display_height//2+50) and y<=(display_height//2+150):
            return (2,2)

def screenMsg(text,size,center):
    myfont = pygame.font.SysFont("Comic Sans MS",size)
    textSurface = myfont.render(text,True,(0,0,0))
    textRect = textSurface.get_rect()
    textRect.center = center
    gameDisplay.blit(textSurface,textRect)


def startScreen():
    global sign
    global csign
    done = False
    #sign = -1
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screenMsg("Let's Play!",150,(display_width//2,display_height//2-150))
            screenMsg("Choose your sign",50,(display_width//2,display_height//2-50))
            drawCross(display_width//2-150,display_height//2)
            drawCircle(display_width//2+50,display_height//2)
            

            pos = pygame.mouse.get_pos()
            
            if pos[0]>(display_width//2-150) and pos[0]<(display_width//2-50):
                if pos[1]>(display_height//2) and pos[1]<(display_height//2+50):
                    if pygame.mouse.get_pressed()[0] == 1:
                        sign = 1
                        csign = 0
                        print(sign)
                        done = True
            if pos[0]>(display_width//2+50) and pos[0]<(display_width//2+150):
                if pos[1]>(display_height//2) and pos[1]<(display_height//2+50):
                    if pygame.mouse.get_pressed()[0] == 1:
                        sign = 0
                        csign = 1
                        print(sign)
                        done = True

            
            
            pygame.display.update()
            #https://youtu.be/dQw4w9WgXcQ
            
            

    

def gameLoop():
    global sign
    global csign

    if csign == 1:
        cmpPlay()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pos()[0] < (display_width//2+150) and pygame.mouse.get_pos()[0]>(display_width//2 - 150):
                if pygame.mouse.get_pos()[1] < (display_height//2 + 150) and pygame.mouse.get_pos()[1] > (display_width//2 - 250):
                    if pygame.mouse.get_pressed()[0] == 1:
                        box = boxLocation(pygame.mouse.get_pos())
                        
                        x,y = getStartingPoint(box)
                        if board[box[0]][box[1]] == -1:

                            board[box[0]][box[1]] = sign
                            if sign==1:
                                drawCross(x,y)
                            elif sign==0:
                                drawCircle(x,y)

                            checkMatch()
                            pygame.display.update()
                            time.sleep(1)
                            cmpPlay()
                            checkMatch()
                        else:
                            continue
            
        pygame.display.update()

def cmpPlay():
    # Try to create the logic where computer chooses its box
    
    global sign
    global csign
    if sign == 1:
        csign = 0
    else:
        csign = 1

    if (-1 in board[0] or -1 in board[1] or -1 in board[2]):
        while True:

            x = randint(0,2)
            y = randint(0,2)

            if board[x][y] == -1:
                board[x][y] = csign
                p,q = getStartingPoint((x,y))

                if csign == 1:
                    drawCross(p,q)
                    
                elif csign == 0:
                    drawCircle(p,q)
                break
            
    
def checkMatch():
    if not (-1 in board[0] or -1 in board[1] or -1 in board[2]):
        winnerScreen("Game Draw")
    if board[0][0] == board[0][1] == board[0][2]:
        checkWinner(board[0][0])
    elif board[0][0] == board[1][1] == board[2][2]:
        checkWinner(board[0][0])
    elif board[0][0] == board[1][0] == board[2][0]:
        checkWinner(board[0][0])
    elif board[0][1] == board[1][1] == board[2][1]:
        checkWinner(board[0][1])
    elif board[0][2] == board[1][2] == board[2][2]:
        checkWinner(board[0][2])
    elif board[1][0] == board[1][1] == board[1][2]:
        checkWinner(board[1][0])
    elif board[2][0] == board[2][1] == board[2][2]:
        checkWinner(board[2][0])
    elif board[2][0] == board[1][1] == board[0][2]:
        checkWinner(board[2][0])
        

def checkWinner(w):
    global sign
    global csign
    if w == sign:
        winnerScreen("Player Won")
    elif w == csign:
        winnerScreen("Computer Won")
        
def winnerScreen(winner):
    pygame.display.update()
    print("Winner")
    time.sleep(1)

    gameDisplay.fill(white)
    gameDisplay.blit(clemson, (225, 450))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screenMsg(winner,100,(display_width//2,display_height//4-100))
            screenMsg("Wanna Play Again??",50,(display_width//2,display_height//4))


            pygame.draw.rect(gameDisplay,black,(display_width//2-75,(display_height//4)+75,50,50))
            pygame.draw.rect(gameDisplay,black,(display_width//2+25,(display_height//4)+75,50,50))

            screenMsg("Yes",50,(display_width//2-50,display_height//4+50))
            screenMsg("No",50,(display_width//2+50,display_height//4+50))

            pos = pygame.mouse.get_pos()

            if (display_width//2-75<=pos[0]<=(display_width//2-75)+50) and ((display_height//4)+75<=pos[1]<=((display_height//4)+75)+50):
                print("Yes")
                if pygame.mouse.get_pressed()[0] == 1:
                    gameReset()
                
            if (display_width//2+25<=pos[0]<=(display_width//2+25)+50) and ((display_height//4)+75<=pos[1]<=((display_height//4)+75)+50):
                print("No")
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()

def gameReset():

    gameDisplay.fill(white)
    gameDisplay.blit(clemson, (225, 450))

    global board
    board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    global sign
    global csign
    sign = None
    csign = None
    
    startScreen()
    drawBoard()
    gameLoop()
            
# rename main function perhaps
startScreen()
drawBoard()
gameLoop()
