import pygame
import random
import moviepy.editor as mp
import sys
import os
import time
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

def main():
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("벤조디아제핀")
    _intro_vid = mp.VideoFileClip("assets/videos/intro.mp4")
    intro_vid = _intro_vid.resize(height=768)
    keepRunning = True
    execPath = sys.executable + " ./gamert.py"
    clk = pygame.time.Clock() # Sorry for dirty names; clock was already defined in other module
    pixelFont_128 = pygame.font.Font("assets/fonts/neodgm.ttf", 128)
    pixelFont_64 = pygame.font.Font("assets/fonts/neodgm.ttf", 64)
    pixelFont_32 = pygame.font.Font("assets/fonts/neodgm.ttf", 32)
    pixelFont_80 = pygame.font.Font("assets/fonts/neodgm.ttf", 80)

    bzdzph_molecule = pygame.image.load("assets/images/bzd.png")
    bzdzph_molecule = pygame.transform.scale(bzdzph_molecule, (300, 200))

    pygame.mouse.set_visible(False)

    # Draw Screen Here:
    # introvidrect = pygame.Rect(100, 100, 640, 360)
    intro_vid.preview()
    # screen.fill((255, 255, 255))
    screen.fill((0, 0, 0))
    pygame.display.update()
    time.sleep(1)
    screen.fill((255, 255, 255))
    titleText = pixelFont_128.render("Benzodiazepine", False, (0, 0, 0))
    titleText_kor = pixelFont_64.render("벤조디아제핀", False, (0, 0, 0))
    playText = pixelFont_80.render("플레이", False, (0, 0, 0))
    creditText = pixelFont_80.render("크레딧", False, (0, 0, 0))
    quitText = pixelFont_80.render("종료", False, (0, 0, 0))
    helpText = pixelFont_32.render("WASD 또는 방향키로 조작하고 스페이스바로 선택", True, (0, 0, 0))
    selectText = pixelFont_80.render("►", False, (0, 0, 0))
    screen.blit(titleText, (250, 100))
    screen.blit(titleText_kor, (500, 250))
    screen.blit(playText, (600, 400))
    screen.blit(quitText, (600, 600))
    screen.blit(creditText, (600, 500))
    screen.blit(helpText, (600, 1000))
    pygame.display.update()

    selXPos = 500
    selYPos = 400
    posStatus = 1

    while keepRunning:
        clk.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepRunning = False
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and 390 < selYPos < 510:
                    selYPos = selYPos + 100
                    posStatus += 1
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and 490 < selYPos < 610:
                    selYPos = selYPos - 100
                    posStatus -= 1
                """
                ---------TODO--------
                 - add main program launch sequence
                 - add credits screen
                """
                if event.key == pygame.K_SPACE:
                    if posStatus == 1:
                        # exec(open('./gamert.py').read())
                        os.system(execPath + " 0 1366 768")
                        # pygame.quit()
                        sys.exit()
                    elif posStatus == 2:
                        pass # TODO: insert here
                    elif posStatus == 3:
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # x = random.randrange(0, 1800)
                # y = random.randrange(0, 900)
                # deg = random.randrange(0, 360)
                # bzdzph_molecule = pygame.transform.rotate(bzdzph_molecule, deg)
                # screen.blit(bzdzph_molecule, (x, y))


            pygame.draw.rect(screen, (255, 255, 255), (500, 400, 95, 350))
            screen.blit(selectText, (selXPos, selYPos))
            pygame.display.update()

if __name__ == '__main__':
    main()
