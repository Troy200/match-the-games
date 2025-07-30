import pygame

pygame.init()

WIDTH=600
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("light blue")

score=0


cc=pygame.image.load("pro game devloper/match the games/images/candycrush.jpg")
ludo=pygame.image.load("pro game devloper/match the games/images/ludo.png")
ss=pygame.image.load("pro game devloper/match the games/images/subwaysurfer.png")
tr=pygame.image.load("pro game devloper/match the games/images/templerun.png")
ccrect=pygame.Rect(75,120,90,90)
ludorect=pygame.Rect(75,240,90,90)
ssrect=pygame.Rect(75,360,90,90)
trrect=pygame.Rect(75,480,90,90)
screen.blit(cc,ccrect)
screen.blit(ludo,ludorect)
screen.blit(ss,ssrect)
screen.blit(tr,trrect)

font1=pygame.font.SysFont("Arial",40)
font2=pygame.font.SysFont("Arial",25)
scoretext= font1.render("score= "+str(score),True,"black")
screen.blit(scoretext,(0,0))
cctext= font2.render("Candy Crush",True,"black")
screen.blit(cctext,(450,360))
ludotext= font2.render("Ludo",True,"black")
screen.blit(ludotext,(450,120))
sstext= font2.render("Subway Surfers",True,"black")
screen.blit(sstext,(450,480))
trtext= font2.render("Temple Run ",True,"black")
screen.blit(trtext,(450,240))



run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()
