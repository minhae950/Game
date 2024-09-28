import sys
try:
    import pygame
    import tkinter
    import ursina
    import moviepy.editor as mp
    import sys
    import subprocess
    import time
    import PIL
except:
    print("============ERROR==============\nMissing Dependencies...\nFollowing Modules are required to run:\n - tkinter\n - pygame\n - moviepy\n - ursina\n - PIL\nPress any Key to Continue...")
    input()
    sys.exit()

PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

def main():
    try:
        configfile = open("config.txt", 'r')
    except:
        print("Config File Not Found: This Program might be corrupt.\n Download the Full Package again and Continue...")
        sys.exit()

    config = configfile.readlines()
    volumeCfg = config[1][:-1]
    widthCfg = config[4][:-1]
    heightCfg = config[5]
    configfile.close()

    parsed_vol = int(volumeCfg) / 100

    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    pygame.display.set_caption("벤조디아제핀")
    _intro_vid = mp.VideoFileClip("assets/videos/intro.mp4")
    intro_vid = _intro_vid.resize(height=768)
    keepRunning = True
    clk = pygame.time.Clock()
    pixelFont_128 = pygame.font.Font("assets/fonts/neodgm.ttf", 128)
    pixelFont_64 = pygame.font.Font("assets/fonts/neodgm.ttf", 64)
    pixelFont_32 = pygame.font.Font("assets/fonts/neodgm.ttf", 32)
    pixelFont_80 = pygame.font.Font("assets/fonts/neodgm.ttf", 80)

    bzdzph_molecule = pygame.image.load("assets/images/bzd.png")
    bzdzph_molecule = pygame.transform.scale(bzdzph_molecule, (300, 200))

    pygame.mouse.set_visible(False)

    intro_sfx = pygame.mixer.Sound('assets/music/intro_effect.mp3')
    intro_sfx.set_volume(0.5 * parsed_vol)
    intro_sfx.play()
    # Draw Screen Here:
    intro_vid.preview()

    background_music = pygame.mixer.Sound('assets/music/alone-musikal.mp3')
    # time.sleep(2.3)
    # time.sleep(1)
    background_music.set_volume(0.3 * parsed_vol)
    background_music.play()
    # print(background_music.get_volume())
    screen.fill((0, 0, 0))
    pygame.display.update()
    time.sleep(0.5)
    screen.fill((255, 255, 255))
    titleText = pixelFont_128.render("Benzodiazepine", False, (0, 0, 0))
    titleText_kor = pixelFont_64.render("벤조디아제핀", False, (0, 0, 0))
    playText = pixelFont_80.render("플레이", False, (0, 0, 0))
    creditText = pixelFont_80.render("크레딧", False, (0, 0, 0))
    quitText = pixelFont_80.render("종료", False, (0, 0, 0))
    settingsText = pixelFont_64.render("설정", False, (0, 0, 0))
    helpText = pixelFont_32.render("WASD 또는 방향키로 조작하고 스페이스바로 선택", True, (0, 0, 0))
    selectText = pixelFont_80.render("►", False, (0, 0, 0))
    screen.blit(titleText, (250, 100))
    screen.blit(titleText_kor, (500, 250))
    screen.blit(playText, (600, 400))
    screen.blit(quitText, (600, 600))
    screen.blit(creditText, (600, 500))
    screen.blit(settingsText, (1200, 680))
    screen.blit(helpText, (300, 730))
    pygame.display.update()

    selXPos = 500
    selYPos = 400
    posStatus = 1
    isSettingSelected = False

    while keepRunning:
        clk.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepRunning = False
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) or (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    isSettingSelected = not isSettingSelected
                    if selXPos == 500:
                        selXPos = 1100
                        selYPos = 670
                    else:
                        selXPos = 500
                        selYPos = 400
                        posStatus = 1
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and 390 < selYPos < 510 and isSettingSelected == False:
                    selYPos = selYPos + 100
                    posStatus += 1
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and 490 < selYPos < 610 and isSettingSelected == False:
                    selYPos = selYPos - 100
                    posStatus -= 1
               
                if event.key == pygame.K_SPACE:
                    if isSettingSelected == True:
                        # subprocess.Popen(args=[sys.executable, "editPref.py"])
                        # exec(open('editPref.py').read())
                        subprocess.Popen(args=[sys.executable, "editPref.py"])
                    elif posStatus == 1:
                        subprocess.Popen(args=[sys.executable, "game.py", volumeCfg, widthCfg, heightCfg])
                        keepRunning = False
                    elif posStatus == 2:
                        pygame.draw.rect(screen, (0, 0, 0), (100, 100, 1170, 600))
                        crTitleText = pixelFont_80.render("Credits", False, (255, 255, 255))
                        screen.blit(crTitleText, (560, 150))
                        crMainText1l1 = pixelFont_32.render("사용한 폰트:", False, (255, 255, 255))
                        crMainText1l2 = pixelFont_32.render("- Copyright (c) 2017-2024, Eunbin Jeong (Dalgona.) ", False, (255, 255, 255))
                        crMainText1l3 = pixelFont_32.render(" <project-neodgm@dalgona.dev> / with reserved font name", False, (255, 255, 255))
                        crMainText1l4 = pixelFont_32.render(" \"Neo둥근모\" and \"NeoDunggeunmo\"", False, (255, 255, 255))
                        # Sound Effect from <a href="https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=6066">Pixabay</a>
                        crMainText2 = pixelFont_32.render("Credit Text 2", False, (255, 255, 255))
                        # crContinueText = pixelFont_32.render("스페이스를 눌러 계속...", False, (255, 255, 255))
                        screen.blit(crMainText1l1, (200, 250))
                        screen.blit(crMainText1l2, (200, 290))
                        screen.blit(crMainText1l3, (200, 330))
                        screen.blit(crMainText1l4, (200, 370))
                        # screen.blit(crContinueText, (500, 650))
                        pygame.display.update()
                        time.sleep(2)
                        pygame.draw.rect(screen, (0, 0, 0), (100, 100, 1170, 600))
                        screen.blit(crTitleText, (560, 150))
                        screen.blit(crMainText2, (200, 250))
                        pygame.display.update()
                        time.sleep(2)
                        
                    elif posStatus == 3:
                        pygame.quit()
                        sys.exit()
                        keepRunning = False

            screen.fill((255, 255, 255))
            screen.blit(titleText, (250, 100))
            screen.blit(titleText_kor, (500, 250))
            screen.blit(playText, (600, 400))
            screen.blit(quitText, (600, 600))
            screen.blit(creditText, (600, 500))
            screen.blit(helpText, (300, 730))
            screen.blit(settingsText, (1200, 680))
            pygame.display.update()

            screen.blit(selectText, (selXPos, selYPos))
            pygame.display.update()

if __name__ == '__main__':
    main()
