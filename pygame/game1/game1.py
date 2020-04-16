import pygame
pygame.init()

win=pygame.display.set_mode((500,400))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg1.jpg')
char = pygame.image.load('standing.png')
icon=pygame.image.load('icon.png')

pygame.display.set_icon(icon)

clock=pygame.time.Clock()
class player():
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
# x=50
# y=416
# width=64
# height=64
# vel=5
# isJump=False
# jumpCount=10
# left=False
# right=False
# walkcount=0
    def draw(self,win):
        if (self.walkcount+1>=27):
            self.walkcount=0
        if (self.left):
            win.blit(walkLeft[self.walkcount//3],(self.x,self.y))
            self.walkcount+=1
        elif(self.right):
            win.blit(walkRight[self.walkcount//3],(self.x,self.y))
            self.walkcount+=1
        else:
            win.blit(char,(self.x,self.y))


def redrawGameWindow():
        win.fill((0,0,0))
        win.blit(bg,(0,0))#bg_image
        man.draw(win)
        pygame.display.update()

man=player(300,300,64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if(man.x!=0):
            man.x=man.x-man.vel
            man.left=True
            man.right=False
    elif keys[pygame.K_RIGHT]:
        if(man.x!=460):
            man.x=man.x+man.vel
            man.left=False
            man.right=True
    else:
        man.left=False
        man.right=False
        man.walkcount=0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump=True
            man.left=False
            man.right=False
            man.walkcount=0
    else:
        if man.jumpCount>=-10:
            neg=1
            if(man.jumpCount<0):
                neg=-1
            man.y-=(man.jumpCount**2)*0.3*neg
            man.jumpCount-=1

        else:
            man.isJump=False
            man.jumpCount=10

    redrawGameWindow()

pygame.quit()
