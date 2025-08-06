import pygame

pygame.init()

WIDTH=600
HEIGHT=720

screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("light blue")

score=0



cc=pygame.image.load("pro game devloper/match the games/images/candycrush.jpg")
ludo=pygame.image.load("pro game devloper/match the games/images/ludo.png")
ss=pygame.image.load("pro game devloper/match the games/images/subwaysurfer.png")
tr=pygame.image.load("pro game devloper/match the games/images/templerun.png")
ttxsize=pygame.image.load("pro game devloper/match the games/images/talkingtom-removebg-preview.png")
tt=pygame.transform.scale(ttxsize,(90,90))

ccrect=pygame.Rect(75,120,90,90)
ludorect=pygame.Rect(75,240,90,90)
ssrect=pygame.Rect(75,360,90,90)
trrect=pygame.Rect(75,480,90,90)
ttrect=pygame.Rect(75,600,90,90)

screen.blit(cc,ccrect)
screen.blit(ludo,ludorect)
screen.blit(ss,ssrect)
screen.blit(tr,trrect)
screen.blit(tt,ttrect)

font1=pygame.font.SysFont("Arial",40)
font2=pygame.font.SysFont("Arial",25)

scoretext= font1.render("score= "+str(score),True,"black")
screen.blit(scoretext,(0,0))

cctext= font2.render("Candy Crush",True,"black")
cctextrect=pygame.Rect(400,390,180,40)
screen.blit(cctext,cctextrect)

ludotext= font2.render("Ludo",True,"black")
ludotextrect=pygame.Rect(400,150,180,40)
screen.blit(ludotext,ludotextrect)

sstext= font2.render("Subway Surfers",True,"black")
sstextrect=pygame.Rect(400,510,180,40)
screen.blit(sstext,sstextrect)

trtext= font2.render("Temple Run ",True,"black")
trtextrect=pygame.Rect(400,630,180,40)
screen.blit(trtext,trtextrect)

tttext= font2.render("Tlaking Tom",True,"black")
tttextrect=pygame.Rect(400,270,180,40)
screen.blit(tttext,tttextrect)
pygame.display.update()
rightanswers=[(ccrect,cctextrect),(ludorect,ludotextrect),(ssrect,sstextrect),(trrect,trtextrect),(ttrect,tttextrect)]
startpos=None
endpos=None
startrect=None
endrect=None

run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()

        elif event.type== pygame.MOUSEBUTTONDOWN:
            startpos=pygame.mouse.get_pos()
            clickedonvalidarea=False
            for imagerect,textrect in rightanswers:
                if imagerect.collidepoint(startpos):
                    clickedonvalidarea=True
                    startrect=imagerect
                    break
            if clickedonvalidarea:
                pygame.draw.circle(screen,"black",startpos,10)
                pygame.display.update() 
        elif event.type== pygame.MOUSEBUTTONUP:
            endpos=pygame.mouse.get_pos()
            releaseonvalidarea=False
            for imagerect,textrect in rightanswers:
                if textrect.collidepoint(endpos):
                    releaseonvalidarea=True
                    endrect=textrect
                    break
            if clickedonvalidarea and releaseonvalidarea:
                pygame.draw.circle(screen,"black",startpos,10)
                pygame.display.update()

    
