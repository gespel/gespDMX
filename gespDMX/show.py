from gespDMXLib import *
import signal, os
import pygame, sys
from pygame.locals import *

gD = gespDMX()

all_processes = []

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()
BLACK = (0,0,0)

WIDTH = 1000
HEIGHT = 800

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("GeDMX - Lichtsteuerungssoftware")
font = pygame.font.SysFont("MS Arial", 30)
creditFont = pygame.font.SysFont("MS Arial", 20)

qV, wV, eV, uV, iV, oV, vV, bV, aV, sV = 0,0,0,0,0,0,0,0,0,0

def drawGui(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
    windowSurface.fill(BLACK)
    creditLabel = creditFont.render("by Sten (d3ler) Heimbrodt", 1, white)
    windowSurface.blit(creditLabel, (835, 785))

    qLabel = font.render("q -> Sweeper_1: ", 1, green)
    windowSurface.blit(qLabel, (10, 10))
    if v1 == 1:
        qLabelAct = font.render("An", 1, green)
    else:
        qLabelAct = font.render("Aus ", 1, green)
    windowSurface.blit(qLabelAct, (190, 10))

    wLabel = font.render("w -> Sweeper_2: ", 1, green)
    windowSurface.blit(wLabel, (10, 50))
    if v2 == 1:
        wLabelAct = font.render("An", 1, green)
    else:
        wLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(wLabelAct, (190, 50))

    eLabel = font.render("e -> Sweeper_3: ", 1, green)
    windowSurface.blit(eLabel, (10, 90))
    if v3 == 1:
        eLabelAct = font.render("An", 1, green)
    else:
        eLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(eLabelAct, (190, 90))

    aLabel = font.render("a -> Sweeper_4: ", 1, green)
    windowSurface.blit(aLabel, (10, 240))
    if v9 == 1:
        aLabelAct = font.render("An", 1, green)
    else:
        aLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(aLabelAct, (190, 240))

    sLabel = font.render("s -> Sweeper_5: ", 1, green)
    windowSurface.blit(sLabel, (10, 280))
    if v10 == 1:
        sLabelAct = font.render("An", 1, green)
    else:
        sLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(sLabelAct, (190, 280))

    uLabel = font.render("u -> Orgel_1: ",1 ,green)
    windowSurface.blit(uLabel, (400,10))
    if v4 == 1:
        uLabelAct = font.render("An",1,green)
    else:
        uLabelAct = font.render("Aus",1,green)
    windowSurface.blit(uLabelAct, (580, 10))

    iLabel = font.render("i -> Orgel_2: ", 1, green)
    windowSurface.blit(iLabel, (400, 50))
    if v5 == 1:
        iLabelAct = font.render("An", 1, green)
    else:
        iLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(iLabelAct, (580, 50))

    oLabel = font.render("o -> Orgel_3: ", 1, green)
    windowSurface.blit(oLabel, (400, 90))
    if v6 == 1:
        oLabelAct = font.render("An", 1, green)
    else:
        oLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(oLabelAct, (580, 90))

    vLabel = font.render("v -> Vbar_1: ", 1, green)
    windowSurface.blit(vLabel, (10, 150))
    if v7 == 1:
        vLabelAct = font.render("An", 1, green)
    else:
        vLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(vLabelAct, (190, 150))

    bLabel = font.render("b -> Vbar_2: ", 1, green)
    windowSurface.blit(bLabel, (10, 190))
    if v8 == 1:
        bLabelAct = font.render("An", 1, green)
    else:
        bLabelAct = font.render("Aus", 1, green)
    windowSurface.blit(bLabelAct, (190, 190))

    pygame.display.flip()

drawGui(qV,wV,eV,uV,iV,oV,vV,bV,aV,sV)
print("Gui wurde geladen!")

while True:
    #get all the user events
    for event in pygame.event.get():

        #if user wants to quit
        if event.type == pygame.locals.QUIT:
            #and the game close the window
            pygame.quit()
            sys.exit()

        #if a key is pressed
        elif event.type == pygame.locals.KEYDOWN:
            #if right arrow is pressed
            if event.key == K_q:
                process = multiprocessing.Process(name="q", target=gD.runFile, args=["sweeper"])
                process.start()
                q = process.pid
                qV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_w:
                process = multiprocessing.Process(name="w", target=gD.runFile, args=["sweeper2"])
                process.start()
                w = process.pid
                wV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_e:
                process = multiprocessing.Process(name="e", target=gD.runFile, args=["sweeper3"])
                process.start()
                e = process.pid
                eV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_u:
                process = multiprocessing.Process(name="u", target=gD.runFile, args=["orgel"])
                process.start()
                u = process.pid
                uV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_i:
                process = multiprocessing.Process(name="i", target=gD.runFile, args=["orgel2"])
                process.start()
                i = process.pid
                iV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_o:
                process = multiprocessing.Process(name="o", target=gD.runFile, args=["orgel3"])
                process.start()
                o = process.pid
                oV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_v:
                process = multiprocessing.Process(name="v", target=gD.runFile, args=["vbar1"])
                process.start()
                v = process.pid
                vV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_b:
                process = multiprocessing.Process(name="b", target=gD.runFile, args=["vbar2"])
                process.start()
                b = process.pid
                bV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_a:
                process = multiprocessing.Process(name="a", target=gD.runFile, args=["sweeper4"])
                process.start()
                a = process.pid
                aV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_s:
                process = multiprocessing.Process(name="s", target=gD.runFile, args=["sweeper5"])
                process.start()
                s = process.pid
                sV = 1
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_y:
                process = multiprocessing.Process(name="b", target=gD.runFile, args=["blackoutSweeper"])
                process.start()
                b = process.pid

        elif event.type == pygame.locals.KEYUP:
            if event.key == K_q:
                os.kill(q, signal.SIGKILL)
                gD.runFileOnce("blackoutSweeper")
                qV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_w:
                os.kill(w, signal.SIGKILL)
                gD.runFileOnce("blackoutSweeper")
                wV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_e:
                os.kill(e, signal.SIGKILL)
                gD.runFileOnce("blackoutSweeper")
                eV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_u:
                os.kill(u, signal.SIGKILL)
                gD.runFileOnce("blackoutOrgel")
                uV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_i:
                os.kill(i, signal.SIGKILL)
                gD.runFileOnce("blackoutOrgel")
                iV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_o:
                os.kill(o, signal.SIGKILL)
                gD.runFileOnce("blackoutOrgel")
                oV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_v:
                os.kill(v, signal.SIGKILL)
                gD.runFileOnce("blackoutVbar")
                vV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_b:
                os.kill(b, signal.SIGKILL)
                gD.runFileOnce("blackoutVbar")
                bV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_a:
                os.kill(a, signal.SIGKILL)
                gD.runFileOnce("blackoutSweeper")
                aV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_s:
                os.kill(s, signal.SIGKILL)
                gD.runFileOnce("blackoutSweeper")
                sV = 0
                drawGui(qV, wV, eV, uV, iV, oV, vV, bV, aV, sV)
            if event.key == K_y:
               os.kill(b, signal.SIGKILL)
    pygame.display.update()