import pygame
import time
import random

pygame.init()
disp_width=800
disp_heig=600
green=(0,155,0)
red=(255,0,0)
orange=(255,69,0)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
aqua=(0,255,255)
yellow=(255,255,0)
gameDisplay=pygame.display.set_mode([disp_width,disp_heig])
pygame.display.set_caption('avi')
icon=pygame.image.load('front.jpg')
skin=pygame.image.load('skin.jpg')
colors = [green,red,orange,white,black,blue,aqua,yellow]

img = pygame.image.load('snakehead.png')
img1= pygame.image.load('apple2.jpg')
smallfont = pygame.font.SysFont("Purisa",25)
medfont = pygame.font.SysFont("Purisa",50)
largefont = pygame.font.SysFont("Purisa",80)

pygame.display.update()

def screen_obj(msg,color,size):
    if size =="medium":
        textsurface=medfont.render(msg,True,color)
    elif size =="small":
        textsurface=smallfont.render(msg,True,color)
    elif size =="large":
        textsurface=largefont.render(msg,True,color)
    
    return textsurface,textsurface.get_rect()

def score(score):
    text=smallfont.render("Score: "+str(score) ,True , orange)
    gameDisplay.blit(text ,[0,0])

def toscreen(msg,color,y_displace,size="small"):
    ##    text=font.render(msg,True,color)
    ##    gameDisplay.blit(text,[disp_width/2-len(msg),disp_heig/2])
    textsurf,textrect= screen_obj(msg,color,size)
    textrect.center =(disp_width/2 , disp_heig /2 + y_displace)
    gameDisplay.blit(textsurf,textrect)

block_size=20
AppleThickness=20
clock=pygame.time.Clock()
direction ="right"

def pause():
    paused = True
    toscreen("GAME PAUSED!!.",black,-50)
    toscreen("Press c to continuo or n to start a new game",green,100)
    pygame.display.update()
    while paused:
        
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                if event.key == pygame.K_n:
                    gameloop()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
    



def game_intro():
    intro = True
    while intro:
        gameDisplay.fill(aqua)
        toscreen("WELCOME TO AVI'S GAME",orange,-100,"medium")
        toscreen("PRESS Y TO START THE GAME",orange,-20,"small")
        gameDisplay.blit(icon,(disp_width/2 - 120 , disp_heig/2 +25 ) )
        text=smallfont.render("pause the game by pressing p at any time",True , orange)
        gameDisplay.blit(text ,[0,0])

        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    intro= False
                    gameloop()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                            
        
        
    
        
def snake(block_size,snakelist):
    if direction == "right":
        head=pygame.transform.rotate(img,270)
        
    if direction == "left":
        head=pygame.transform.rotate(img,90)

    if direction == "up":
        head=img

    if direction == "down":
        head=pygame.transform.rotate(img,180)

    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))

    for xny in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,green,[xny[0],xny[1],block_size,block_size])
        #gameDisplay.blit(skin,(xny[0],xny[1]))

def gameloop():
    global direction
    
    gameexit= False
    gameover = False
    
    snakelist=[]
    snakelength=1
    gameDisplay=pygame.display.set_mode([disp_width,disp_heig])
    
    lead_x=disp_width/2
    lead_y=disp_heig/2
    lead_x_change=0
    lead_y_change=0
    randx=round(random.randrange(AppleThickness,disp_width-AppleThickness))#/10.0)*10.0;
    randy=round(random.randrange(AppleThickness,disp_heig -AppleThickness))#/10.0)*10.0;
   
   
    

    while not gameexit:

        while gameover ==True:
            gameDisplay.fill(aqua)
            toscreen("Game Over",red,-50,size="medium")
            toscreen("Press c to play again or q to quit",orange,50,size="small")
            toscreen("YOUR SCORE IS",orange,80,size="small")
            toscreen(str(snakelength-1),green,100,size="small")
          

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit=True
                    gameover=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop()
                    if event.key == pygame.K_q:
                        gameexit=True
                        gameover=False
            pygame.display.update()                            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    lead_x_change=-block_size
                    lead_y_change=0
                    direction = "left"
                if event.key == pygame.K_d:
                    lead_x_change=block_size
                    lead_y_change=0
                    direction = "right"
                if event.key == pygame.K_w:
                    lead_y_change=-block_size
                    lead_x_change=0
                    direction = "up"
                if event.key == pygame.K_s:
                    lead_y_change=block_size
                    lead_x_change=0
                    direction = "down"
                if event.key == pygame.K_p:
                    pause()
                        
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(white)
        gameDisplay.blit(img1,(randx,randy) )
        
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameover=True
                 
                
    
        snake(block_size,snakelist)
        
        if lead_x >=disp_width or lead_x <0 or lead_y >=disp_heig or lead_y <0:
            gameover=True

        score(snakelength-1)
        
        pygame.display.update()
##        if lead_x == randx and lead_y == randy:
##            randx=round(random.randrange(block_size,disp_width-block_size)/10.0)*10.0;
##            randy=round(random.randrange(block_size,disp_heig -block_size)/10.0)*10.0;
##            snakelength+=1

        if lead_x >= randx and lead_x < randx + AppleThickness or lead_x + block_size >= randx and lead_x + block_size < randx + AppleThickness :
            if lead_y >= randy and lead_y < randy + AppleThickness or lead_y + block_size >= randy and lead_y + block_size < randy + AppleThickness :
                randx=round(random.randrange(block_size,disp_width-block_size))#/10.0)*10.0;
                randy=round(random.randrange(block_size,disp_heig -block_size))#/10.0)*10.0;
                snakelength+=1


        clock.tick(25)



    time.sleep(2)
    pygame.quit()
    quit()

game_intro()

        
