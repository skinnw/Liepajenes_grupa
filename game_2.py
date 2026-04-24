import pygame
import time
# Inicializē Pygame bibliotēku
pygame.init()

# Krāsas
WHT, BLK, GRY, LGRY, W98, DW98 = (255,255,255), (0,0,0), (100,100,100), (150,150,150), (200, 157, 124), (125, 102, 93)
DRED, RED = (50,0,0), (255,0,0)
# Loga izšķirtspēja
dwidth, dheight = 800, 600
#Teksta objekti
def txt_objects(text, font):
    textSurface = font.render(text, True, BLK)
    return textSurface, textSurface.get_rect()

def draw_score():
    global score
    score_text = smalltxtfont.render(f"Punkti: {score}", True, BLK)
    pygame.draw.rect(screen, LGRY, (10, 10, 150, 40))  # background box
    screen.blit(score_text, (15, 15))

lvlpopup = True
IsRunning = True
score = 0
points = 5
visited1 = False
visited2 = False
visited3 = False
visited4 = False
visited5 = False
visited6 = False
visited7 = False
visited8 = False
visited9 = False
visited10 = False


class buttons:
            def __init__(self, xcoord, ycoord, xsize, ysize, idlecolor, activecolor, completion):
                self.xcoord = xcoord
                self.ycoord = ycoord
                self.xsize = xsize
                self.ysize = ysize
                self.idlecolor = idlecolor
                self.activecolor = activecolor
                self.completion = completion
                self.mouse = pygame.mouse.get_pos()
                if self.completion == True:
                    self.xcoord = -9999
                    self.ycoord = -9999
            def button(self):
                if self.xcoord <= self.mouse[0] <= self.xcoord + self.xsize and self.ycoord  <= self.mouse[1] <= self.ycoord + self.ysize:
                    pygame.draw.rect(screen, self.idlecolor, (self.xcoord , self.ycoord ,self.xsize ,self.ysize))
                else:
                     pygame.draw.rect(screen, self.activecolor, (self.xcoord , self.ycoord ,self.xsize ,self.ysize))

                

class text(buttons):
            def  __init__(self ,text ,color ,xcoord ,ycoord ,xsize, ysize):
                self.text = text
                self.color = color
                self.xcoord = xcoord
                self.ycoord = ycoord
                self.xsize = xsize
                self.ysize = ysize
                self.mouse = pygame.mouse.get_pos()
            def showbtext(self):
                    UItxt = btnfont.render(self.text, True, self.color) 
                    screen.blit(UItxt, (self.xcoord + 5, self.ycoord + 5)) 
            def showtext(self):
                    UItxt = smalltxtfont.render(self.text, True, self.color) 
                    screen.blit(UItxt, (self.xcoord , self.ycoord)) 
            def showltext(self):
                    UItxt = txtfont.render(self.text, True, self.color) 
                    screen.blit(UItxt, (self.xcoord , self.ycoord)) 
            def showmaptext(self):
                if self.xcoord  <= self.mouse[0] <= self.xcoord + self.xsize and self.ycoord  <= self.mouse[1] <= self.ycoord + self.ysize:
                    UItxt = txtfont.render(self.text, True, self.color) 
                    screen.blit(UItxt, (20, 500)) 
            def titletext(self):
                TextSurf, TextRect = txt_objects(self.text, titlefont)
                TextRect.center = (self.xcoord, self.ycoord)
                screen.blit(TextSurf, TextRect)


# Izveido spēles logu
screen = pygame.display.set_mode((dwidth, dheight))
pygame.display.set_caption("Mācību ekskursija Liepājā")
clock = pygame.time.Clock()


titlefont = pygame.font.Font('freesansbold.ttf',60)
btnfont = pygame.font.Font('freesansbold.ttf' , 40)
txtfont = pygame.font.Font('freesansbold.ttf' , 35)
smalltxtfont = pygame.font.Font('freesansbold.ttf' , 20)

# Kods 'Par spēli' ekrānam
def about_screen():
    aboutscreen = True
    while aboutscreen:
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.xcoord <= back.mouse[0] <= back.xcoord + back.xsize and back.ycoord <= back.mouse[1] <= back.ycoord + back.ysize:
                    title_screen()
                    aboutscreen = False
                    if ingame_map == True:
                        ingame_map()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.xcoord <= start.mouse[0] <= start.xcoord + start.xsize and start.ycoord <= start.mouse[1] <= start.ycoord + start.ysize:
                    ingame_map()
        
        bg_img = pygame.image.load('liepaja2.jpg')
        bg_img = pygame.transform.scale(bg_img, (dwidth, dheight))
        screen.blit(bg_img, (0, 0))

        pygame.draw.rect(screen, LGRY, (0, (dheight/6) - 60, 800, 350))
        
        info1 = text('Lai kustinātu karti izmantojiet bultiņu pogas uz savas klaviatūras', BLK, 10, (dheight/6 + 50), 0, 0)
        info2 = text('Lai sāktu uzdevumu uzklikšķiniet uz vienu no sarkanajiem kvadrātiem', BLK, 10, (dheight/6 + 70), 0, 0)
        info3 = text('Par katru pareizo atbildi tiek doti 5 punkti', BLK, 10, (dheight/6 + 90), 0, 0)
        info4 = text('Kļūdoties 1 reizi saņemi 3 punktus un kļūdoties 2 reizes saņem tikai 1 punktu.', BLK, 10, (dheight/6 + 110), 0, 0)
        info5 = text('Spēli veidoja Pēteris Poļikovs, Ella Jēkabsone un Valters Jūrmalis', BLK, 10, (dheight/6 + 130), 0, 0)
        info6 = text('Karte ņemta no https://anvaka.github.io/city-roads/?q=Liepāja&areaId=3613048685', BLK, 10, (dheight/6 + 150), 0, 0)
        info7 = text('info par apskates vietām:', BLK, 10, (dheight/6 + 170), 0, 0)
        info8 = text('https://liepaja.travel/', BLK, 10, (dheight/6 + 190), 0, 0)
        info9 = text('https://www.karosta.lv/', BLK, 10, (dheight/6 + 210), 0, 0)
        info10 = text('https://www.liepajasmuzejs.lv/', BLK, 10, (dheight/6 + 230), 0, 0)
        title = text('Par Spēli', BLK, (dwidth/2), (dheight/6), 0, 0)
        title.titletext()

        # Kods pogām
        back = buttons(430, 500, 325, 50, LGRY, GRY, 0)
        backtxt = text('Galvenā Izvēlne', BLK, back.xcoord, back.ycoord, back.xsize, back.ysize)
        start = buttons(50, 500 ,150 ,50, LGRY, GRY, 0)
        starttxt = text('Karte', BLK, start.xcoord, back.ycoord, back.xsize, back.ysize)
        back.button()
        start.button()
        starttxt.showbtext()
        backtxt.showbtext()
        info1.showtext()
        info2.showtext()
        info3.showtext()
        info4.showtext()
        info5.showtext()
        info6.showtext()
        info7.showtext()
        info8.showtext()
        info9.showtext()
        info10.showtext()
        pygame.display.update()
        clock.tick(15)
# Kods titulkadram
def title_screen():
    
    ttlscreen = True
    while ttlscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Funkcionalitāte 'iziet' pogai
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitbtn.xcoord <= mouse[0] <= exitbtn.xcoord + exitbtn.xsize and exitbtn.ycoord <= mouse[1] <= exitbtn.ycoord + exitbtn.ysize:
                    exitpup()
            # Funkcionalitāte 'par spēli' pogai
            if event.type == pygame.MOUSEBUTTONDOWN:
                if aboutbtn.xcoord <= mouse[0] <= aboutbtn.xcoord + aboutbtn.xsize and aboutbtn.ycoord <= mouse[1] <= aboutbtn.ycoord + aboutbtn.ysize:
                   about_screen() 
                   ttlscreen = False
            # Funkcionalitāte 'rezultāti' pogai
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resultbtn.xcoord <= mouse[0] <= resultbtn.xcoord + resultbtn.xsize and resultbtn.ycoord <= mouse[1] <= resultbtn.ycoord + resultbtn.ysize:
                   results_screen() 
            # Funkcionalitāte 'sākt spēli' pogai
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startbtn.xcoord <= mouse[0] <= startbtn.xcoord + startbtn.xsize and startbtn.ycoord <= mouse[1] <= startbtn.ycoord + startbtn.ysize:
                    startpup()
                   
            bg_img = pygame.image.load('liepaja.jpg')
            bg_img = pygame.transform.scale(bg_img, (dwidth, dheight))
            screen.blit(bg_img, (0, 0))
        
        # Peles koordinātes
        mouse = pygame.mouse.get_pos()

        title = text('Mācību Ekskursija Liepājā', BLK, (dwidth/2), (dheight/6), 0, 0)
        pygame.draw.rect(screen, LGRY, (0, (dheight/6) - 60, 800, 150))
        title.titletext()
        
        
        # Kods pogām

        exitbtn = buttons(630, 500 ,120 ,50, LGRY, GRY,0)
        exitbtntext = text("Iziet", BLK, exitbtn.xcoord, exitbtn.ycoord, exitbtn.xsize, exitbtn.ysize)
        aboutbtn = buttons(30, 500 ,205 ,50, LGRY, GRY,0)
        aboutbtntext = text("Par Spēli", BLK, aboutbtn.xcoord, aboutbtn.ycoord, aboutbtn.xsize, aboutbtn.ysize)
        startbtn = buttons(dwidth/2 -150, 225 ,250 ,50, LGRY, GRY,0)
        startbtntext = text("Sākt Spēli", BLK, startbtn.xcoord, startbtn.ycoord, startbtn.xsize, startbtn.ysize)
        resultbtn = buttons(dwidth/2 -150, 330 ,250 ,50, LGRY, GRY,0)
        resultbtntext = text("Rezultāti", BLK, resultbtn.xcoord, resultbtn.ycoord, resultbtn.xsize, resultbtn.ysize)
        greetings = text("Lai sāktu ekskursiju uzspiediet pogu 'Sākt Spēli'!", BLK, dwidth/2 -225, 150, 0 , 0)
        author = text("Autors: 'Binārais Trio', 2026", BLK, 525, 580, 0, 0)
        exitbtn.button()
        exitbtntext.showbtext()
        aboutbtn.button()
        aboutbtntext.showbtext()
        startbtn.button()
        startbtntext.showbtext()
        resultbtn.button()
        resultbtntext.showbtext()
        greetings.showtext()
        author.showtext()
        author = smalltxtfont.render("Autors: 'Binārais Trio', 2026", True , BLK)
        screen.blit(author, (525, 580))
        pygame.display.update()
        clock.tick(15)


# Kods priekš 'Vai jūs vēlaties sākt ekskursiju?'

def startpup():
    startpopup = True
    while startpopup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yesbtn.xcoord <= yesbtn.mouse[0] <= yesbtn.xcoord + yesbtn.xsize and yesbtn.ycoord <= yesbtn.mouse[1] <= yesbtn.ycoord + yesbtn.ysize:
                   ttlscreen = False
                   ingame_map()
                   
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nobtn.xcoord <= nobtn.mouse[0] <= nobtn.xcoord + nobtn.xsize and nobtn.ycoord <= nobtn.mouse[1] <= nobtn.ycoord + nobtn.ysize:
                   startpopup = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               if rulesbtn.xcoord <= rulesbtn.mouse[0] <= rulesbtn.xcoord + rulesbtn.xsize and rulesbtn.ycoord <= rulesbtn.mouse[1] <= rulesbtn.ycoord + rulesbtn.ysize:
                   about_screen()

        pygame.draw.rect(screen, LGRY, (dwidth/4 -75, 250 ,570 ,175))
        starttxt = text("Vai jūs vēlaties sākt ekskursiju?", BLK, dwidth/4 -60, 260 ,0 ,0)
        starttxt.showltext()

        # Kods pogām

        yesbtn = buttons(dwidth/4 -15, 360 ,70 ,50, LGRY, GRY,0)
        yesbtntext = text("Jā", BLK, yesbtn.xcoord, yesbtn.ycoord, yesbtn.xsize, yesbtn.ysize)
        rulesbtn = buttons(dwidth/2 -85, 360 ,205 ,50, LGRY, GRY,0)
        rulesbtntext = text("Noteikumi", BLK, rulesbtn.xcoord, rulesbtn.ycoord, rulesbtn.xsize, rulesbtn.ysize)
        nobtn = buttons(dwidth/2 +175, 360 ,70 ,50, LGRY, GRY,0)
        nobtntext = text("Nē", BLK, nobtn.xcoord, nobtn.ycoord, nobtn.xsize, nobtn.ysize)
        yesbtn.button()
        yesbtntext.showbtext()
        rulesbtn.button()
        rulesbtntext.showbtext()
        nobtn.button()
        nobtntext.showbtext()

        pygame.display.update()
        clock.tick(15)

# Kods 'Vai jūs vēlaties iziet?' logam

def exitpup():
    exitpopup = True
    while exitpopup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yesbtn.xcoord <= yesbtn.mouse[0] <= yesbtn.xcoord + yesbtn.xsize and yesbtn.ycoord <= yesbtn.mouse[1] <= yesbtn.ycoord + yesbtn.ysize:
                   pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nobtn.xcoord <= nobtn.mouse[0] <= nobtn.xcoord + nobtn.xsize and nobtn.ycoord <= nobtn.mouse[1] <= nobtn.ycoord + nobtn.ysize:
                   exitpopup = False

        pygame.draw.rect(screen, DW98, (dwidth/4 -40, 250 ,490 ,175))
        exittxt = text("Vai jūs vēlaties iziet?", BLK, dwidth/4 +10, 260 ,0 ,0)
        exittxt.showltext()

        # Kods pogām
        yesbtn = buttons(dwidth/4 -10, 360 ,70 ,50, LGRY, GRY,0)
        yesbtntext = text("Jā", BLK, yesbtn.xcoord, yesbtn.ycoord, yesbtn.xsize, yesbtn.ysize)
        nobtn = buttons(dwidth/2 +145, 360 ,70 ,50, LGRY, GRY,0)
        nobtntext = text("Nē", BLK, nobtn.xcoord, nobtn.ycoord, nobtn.xsize, nobtn.ysize)
        yesbtn.button()
        yesbtntext.showbtext()
        nobtn.button()
        nobtntext.showbtext()
    
        pygame.display.update()
        clock.tick(15)

# Rezultātu ekrāns

def results_screen():
    rsltscreen = True
    file = open('results.txt' ,encoding= "utf-8")
    content = file.readlines()
    line1 = content[0]
    while rsltscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.xcoord <= back.mouse[0] <= back.xcoord + back.xsize and back.ycoord <= back.mouse[1] <= back.ycoord + back.ysize:
                    rsltscreen = False    
        # Peles koordinātes
        mouse = pygame.mouse.get_pos()
        
        pygame.draw.rect(screen, DW98, (dwidth/4 -40, 180 ,490 ,290))
        starttxt = text("Rezultāti", BLK, dwidth/2 - 80, 190 ,0 ,0)
        res1 = text(line1, BLK, dwidth/2 - 80, 300 ,0 ,0)
        back = buttons(dwidth/2 +50, 400 ,180 ,50, LGRY, GRY,0)
        backtxt = text('Atpakaļ', BLK, back.xcoord, back.ycoord, back.xsize, back.ysize)
        starttxt.showltext()
        back.button()
        backtxt.showbtext()
        res1.showtext()

        draw_score()
        pygame.display.update()

        pygame.display.update()
        clock.tick(15)
# Spēles palaišanas poga


#palaiž spēli
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Kods priekš Liepājas kartes ekrāna


def ending():
    endcard = True
    file = open('results.txt' ,'w',encoding= "utf-8")
    file.write(f"Punkti: {score}")

    while endcard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Funkcionalitāte 'iziet' pogai
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitbtn.xcoord <= exitbtn.mouse[0] <= exitbtn.xcoord + exitbtn.xsize and exitbtn.ycoord <= exitbtn.mouse[1] <= exitbtn.ycoord + exitbtn.ysize:
                    exitpup()
                       
        screen.fill(W98)
        
        title = text('Paldies ka spēlējāt!', BLK, (dwidth/2), (dheight/6), 0, 0)
        title.titletext()
        
        
        # Kods pogām

        exitbtn = buttons(630, 500 ,120 ,50, LGRY, GRY,0)
        exitbtntext = text("Iziet", BLK, exitbtn.xcoord, exitbtn.ycoord, exitbtn.xsize, exitbtn.ysize)
        thanks = text("Jūsu Liepājas ekskursija ir galā!", BLK, dwidth/2 -225, 150, 0 , 0)
        scoreshow = text(f"Jūsu punkti: {score}", BLK, dwidth/2 -225, 170, 0 , 0)
        scoreinfo = text(f"Jūs varat savus rezultātus vēlāk apskatīties rezultāts logā", BLK, dwidth/2 -225, 190, 0 , 0)
        exitbtn.button()
        exitbtntext.showbtext()
        thanks.showtext()
        scoreshow.showtext()
        scoreinfo.showtext()
        pygame.display.update()
        clock.tick(15)
    
        
        

def antisoftlock():
    global visited1, visited2, visited3, visited4, visited5, visited6, visited7, visited8, visited9, visited10
    if levels.last_runner == level1 and lvlpopup == False:
        visited1 = False
    if levels.last_runner == level2 and lvlpopup == False:
        visited2 = False
    if levels.last_runner == level3 and lvlpopup == False:
        visited3 = False
    if levels.last_runner == level4 and lvlpopup == False:
        visited4 = False
    if levels.last_runner == level5 and lvlpopup == False:
        visited5 = False
    if levels.last_runner == level6 and lvlpopup == False:
        visited6 = False
    if levels.last_runner == level7 and lvlpopup == False:
        visited7 = False
    if levels.last_runner == level8 and lvlpopup == False:
        visited8 = False
    if levels.last_runner == level9 and lvlpopup == False:
        visited9 = False
    if levels.last_runner == level10 and lvlpopup == False:
        visited10 = False
    
def ingame_map():
    global visited1, visited2, visited3, visited4, visited5, visited6, visited7, visited8, visited9, visited10, lvlpopup
    if lvlpopup == False:
        visited1 = False
    if visited1 and visited2 and visited3 and visited4 and visited5 and visited6 and visited7 and visited8 and visited9 and visited10:
        lvlpopup = False
        ending()
    # Ielādē attēlu programmā

    img = pygame.image.load('map.png')
    map = img.convert()


    x, y = 0, 0

    ingame = True

    while ingame:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn1.xcoord  <= mapbtn1.mouse[0] <= mapbtn1.xcoord + mapbtn1.xsize and mapbtn1.ycoord <= mapbtn1.mouse[1] <= mapbtn1.ycoord + mapbtn1.ysize:
                    visited1 = True
                    level1.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn2.xcoord  <= mapbtn2.mouse[0] <= mapbtn2.xcoord + mapbtn2.xsize and mapbtn2.ycoord <= mapbtn2.mouse[1] <= mapbtn2.ycoord + mapbtn2.ysize:
                    visited2 = True
                    level2.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn3.xcoord  <= mapbtn3.mouse[0] <= mapbtn3.xcoord + mapbtn3.xsize and mapbtn3.ycoord <= mapbtn3.mouse[1] <= mapbtn3.ycoord + mapbtn3.ysize:
                    visited3 = True
                    level3.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn4.xcoord  <= mapbtn4.mouse[0] <= mapbtn4.xcoord + mapbtn4.xsize and mapbtn4.ycoord <= mapbtn4.mouse[1] <= mapbtn4.ycoord + mapbtn4.ysize:
                    visited4 = True
                    level4.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn5.xcoord  <= mapbtn5.mouse[0] <= mapbtn5.xcoord + mapbtn5.xsize and mapbtn5.ycoord <= mapbtn5.mouse[1] <= mapbtn5.ycoord + mapbtn5.ysize:
                    visited5 = True
                    level5.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn6.xcoord  <= mapbtn6.mouse[0] <= mapbtn6.xcoord + mapbtn6.xsize and mapbtn6.ycoord <= mapbtn6.mouse[1] <= mapbtn6.ycoord + mapbtn6.ysize:
                    visited6 = True
                    level6.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn7.xcoord  <= mapbtn7.mouse[0] <= mapbtn7.xcoord + mapbtn7.xsize and mapbtn7.ycoord <= mapbtn7.mouse[1] <= mapbtn7.ycoord + mapbtn7.ysize:
                    visited7 = True
                    level7.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn8.xcoord  <= mapbtn8.mouse[0] <= mapbtn8.xcoord + mapbtn8.xsize and mapbtn8.ycoord <= mapbtn8.mouse[1] <= mapbtn8.ycoord + mapbtn8.ysize:
                    visited8 = True
                    level8.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn9.xcoord  <= mapbtn9.mouse[0] <= mapbtn9.xcoord + mapbtn9.xsize and mapbtn9.ycoord <= mapbtn9.mouse[1] <= mapbtn9.ycoord + mapbtn9.ysize:
                    visited9 = True
                    level9.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapbtn10.xcoord  <= mapbtn10.mouse[0] <= mapbtn10.xcoord + mapbtn10.xsize and mapbtn10.ycoord <= mapbtn10.mouse[1] <= mapbtn10.ycoord + mapbtn10.ysize:
                    visited10 = True
                    level10.lvlinfo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if aboutbtn.xcoord  <= aboutbtn.mouse[0] <= aboutbtn.xcoord + aboutbtn.xsize and aboutbtn.ycoord <= aboutbtn.mouse[1] <= aboutbtn.ycoord + aboutbtn.ysize:
                    about_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitbtn.xcoord <= exitbtn.mouse[0] <= exitbtn.xcoord + exitbtn.xsize and exitbtn.ycoord <= exitbtn.mouse[1] <= exitbtn.ycoord + exitbtn.ysize:
                    exitpup()
         


        # Kartes kustināšanas kods
        speed = 7
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x += speed
        if keys[pygame.K_RIGHT]:
            x -= speed 
        if keys[pygame.K_UP]:
            y += speed
        if keys[pygame.K_DOWN]:
            y -= speed  
        if x >= -350:
                x = -350
        if x <= -1000:
                x = -1000
        if y >= 0:
                y = 0 
        if y <= -1200:
                y = -1200  
        
        screen.fill(W98)
        screen.blit(map, (x, y))

        #Kartes pogas

        mapbtn1 = buttons((x + 843), (y + 825), 20, 20, RED, DRED, visited1)
        mapbtn2 = buttons((x + 802) ,(y + 1285) ,20 ,20 ,RED, DRED, visited2)
        mapbtn3 = buttons((x + 775) ,(y + 1270) ,20 ,20 ,RED, DRED, visited3)
        mapbtn4 = buttons((x + 815), (y + 777), 20, 20, RED, DRED, visited4)
        mapbtn5 = buttons((x + 726), (y + 1270), 20, 20, RED, DRED, visited5)
        mapbtn6 = buttons((x + 665), (y + 1320), 20, 20, RED, DRED, visited6)
        mapbtn7 = buttons((x + 790) ,(y + 1312), 20, 20, RED, DRED, visited7)
        mapbtn8 = buttons((x + 813) ,(y + 1263), 20, 20, RED, DRED, visited8)
        mapbtn9 = buttons((x + 751) ,(y + 1350), 20, 20, RED, DRED, visited9)
        mapbtn10 = buttons((x + 707), (y + 1280), 20, 20, RED, DRED, visited10)
        mapbtn1.button()
        mapbtn2.button()
        mapbtn3.button()
        mapbtn4.button()
        mapbtn5.button()
        mapbtn6.button()
        mapbtn7.button()
        mapbtn8.button()
        mapbtn9.button()
        mapbtn10.button()

        # UI elementi (apakšējā rinda kartes ekrānā)

        # Izveido apakšējo rindu zem kartes
        pygame.draw.rect(screen, DW98, (0, 490 ,800 ,110))

        aboutbtn = buttons(355, 550 ,205 ,45, LGRY, GRY,0)
        aboutbtntext = text("Noteikumi", BLK, aboutbtn.xcoord, aboutbtn.ycoord, aboutbtn.xsize, aboutbtn.ysize)
        exitbtn = buttons(570, 550 ,205 ,45, LGRY, GRY,0)
        exitbtntext = text("Iziet", BLK, exitbtn.xcoord, exitbtn.ycoord, exitbtn.xsize, exitbtn.ysize)
        aboutbtn.button()
        aboutbtntext.showbtext()
        exitbtn.button()
        exitbtntext.showbtext()

        
        mbtext1 = text("Karostas Cietums", BLK, mapbtn1.xcoord, mapbtn1.ycoord, mapbtn1.xsize, mapbtn1.ysize)
        mbtext2 = text("Sv. Trīsvienības katedrāle" , BLK, mapbtn2.xcoord, mapbtn2.ycoord, mapbtn2.xsize, mapbtn2.ysize)
        mbtext3 = text("Lielais Dzintars", BLK, mapbtn3.xcoord, mapbtn3.ycoord, mapbtn3.xsize, mapbtn3.ysize)
        mbtext4 = text("Sv. Nikolaja pareizticīgo Jūras katedrāle", BLK, mapbtn4.xcoord, mapbtn4.ycoord, mapbtn4.xsize, mapbtn4.ysize)
        mbtext5 = text("Liepājas Muzejs", BLK, mapbtn5.xcoord, mapbtn5.ycoord, mapbtn5.xsize, mapbtn5.ysize)
        mbtext6 = text("Spoku Koks", BLK, mapbtn6.xcoord, mapbtn6.ycoord, mapbtn6.xsize, mapbtn6.ysize)
        mbtext7 = text("Romas Dārzs", BLK, mapbtn7.xcoord, mapbtn7.ycoord, mapbtn7.xsize, mapbtn7.ysize)
        mbtext8 = text("Kārļa Zāles piemineklis", BLK, mapbtn8.xcoord, mapbtn8.ycoord, mapbtn8.xsize, mapbtn8.ysize)
        mbtext9 = text("Sv. Jāzepa katedrāle", BLK, mapbtn9.xcoord, mapbtn9.ycoord, mapbtn9.xsize, mapbtn9.ysize)
        mbtext10 = text("Liepājas himnas tēlu skulptūras", BLK, mapbtn10.xcoord, mapbtn10.ycoord, mapbtn10.xsize, mapbtn10.ysize)
        mbtext1.showmaptext()
        mbtext2.showmaptext()
        mbtext3.showmaptext()
        mbtext4.showmaptext()
        mbtext5.showmaptext()
        mbtext6.showmaptext()
        mbtext7.showmaptext()
        mbtext8.showmaptext()
        mbtext9.showmaptext()
        mbtext10.showmaptext()
        
        draw_score() 
        pygame.display.update()
        clock.tick(60)

# Kods priekš līmeņa izpildes atzīmēšanu

# Kods priekš līmeņiem

class levels:
    last_runner = None
    def __init__(self, name, text1, text2, text3, text4, qstns, ans, posans):
        self.name = name
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4
        self.qstns = qstns
        self.ans = ans
        self.posans = posans
        
    def lvlinfo(self):
        levels.last_runner = self
        global visited1, visited2, visited3, visited4, visited5, visited6, visited7, visited8, visited9, visited10, lvlpopup
        lvlpopup = True
        while lvlpopup:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yesbtn.xcoord <= mouse[0] <= yesbtn.xcoord + yesbtn.xsize and yesbtn.ycoord <= mouse[1] <= yesbtn.ycoord + yesbtn.ysize:
                       
                       self.inlevel()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if nobtn.xcoord <= mouse[0] <= nobtn.xcoord + nobtn.xsize and nobtn.ycoord <= mouse[1] <= nobtn.ycoord + nobtn.ysize:
                       lvlpopup = False
                       antisoftlock()
                       
                       

            # Peles koordinātes
            mouse = pygame.mouse.get_pos()
        

            pygame.draw.rect(screen, DW98, (dwidth/4 -75, 50 ,570 ,375))
            lvlname = text(self.name, BLK, dwidth/4 -60, 60 ,0 ,0)
            lvltxt1 = text(self.text1, BLK, dwidth/4 -60, 100 ,0 ,0)
            lvltxt2 = text(self.text2, BLK, dwidth/4 -60, 125 ,0 ,0)
            lvltxt3 = text(self.text3, BLK, dwidth/4 -60, 150 ,0 ,0)
            lvltxt4 = text(self.text4, BLK, dwidth/4 -60, 175 ,0 ,0)
            lvlname.showltext()
            lvltxt1.showtext()
            lvltxt2.showtext()
            lvltxt3.showtext()
            lvltxt4.showtext()


            # Kods pogām

            yesbtn = buttons(dwidth/4 -60, 360 ,150 ,50, LGRY, GRY,0)
            yesbtntext = text("Sākt", BLK , yesbtn.xcoord, yesbtn.ycoord, yesbtn.xsize, yesbtn.ysize)
            nobtn = buttons(dwidth/2 +120, 360 ,160 ,50, LGRY, GRY,0)
            nobtntext = text("Atpakaļ", BLK , nobtn.xcoord, nobtn.ycoord, nobtn.xsize, nobtn.ysize)
            yesbtn.button()
            yesbtntext.showbtext()
            nobtn.button()
            nobtntext.showbtext()
            
            draw_score()
            pygame.display.update()
            clock.tick(15)
    
    # Resursi līmeņiem (jautājumi, atbildes, utt.)

    def leveldata(self):
        file = open('data.txt' ,encoding= "utf-8")
        content = file.readlines()
        question = content[self.qstns]
        posanswers = content[self.posans]
        posanswers = posanswers.split(',')
        coranswer = content[self.ans]
        return question, posanswers, coranswer
    
    def penalty(self):
        global points
        if points > 1 and points <= 5:
            points -= 2
        return points
   
    def addscore(self):
        global score
        global points
        score += points
        points = 5

    def inlevel(self):
        inlevel = True
        show_wrong = False
        while inlevel:
            
            question, posanswers, coranswer = self.leveldata()
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if frstans.xcoord <= frstans.mouse[0] <= frstans.xcoord + frstans.xsize and frstans.ycoord <= frstans.mouse[1] <= frstans.ycoord + frstans.ysize:
                        if firstans == coranswer.strip():
                            self.addscore()
                            ingame_map()
                            
                        else:
                           show_wrong = True
                           self.penalty()
                           
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if scndans.xcoord <= scndans.mouse[0] <= scndans.xcoord + scndans.xsize and scndans.ycoord <= scndans.mouse[1] <= scndans.ycoord + scndans.ysize:
                        if secondans == coranswer.strip():
                            self.addscore()
                            ingame_map()
                                 
                        else:
                           show_wrong = True

                           
                           self.penalty()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if trdans.xcoord <= trdans.mouse[0] <= trdans.xcoord + trdans.xsize and trdans.ycoord <= trdans.mouse[1] <= trdans.ycoord + trdans.ysize:
                        if thirdans == coranswer.strip():
                            self.addscore()
                            ingame_map()
                            
                        else:
                            show_wrong = True
                            
                            self.penalty()
    

            screen.fill(W98)
            
            question = text(question.strip(), BLK, (dwidth/6), (dheight/6), 0, 0)
            question.showltext()

            if show_wrong:
                screen.blit(wrong, ((dwidth/6) +50, (dheight/2) + 50))     

            wrong = txtfont.render("Nepareizi! Mēģiniet vēlreiz!", True, RED)

            # Kods pogām
            frstans = buttons(50, 500 ,200 ,50, LGRY, GRY,0)
            firstans = posanswers[0].strip()
            frstanstext = text(posanswers[0].strip(), BLK, frstans.xcoord, frstans.ycoord, frstans.xsize, frstans.ysize)
            scndans = buttons(300, 500 ,200 ,50, LGRY, GRY,0)
            secondans = posanswers[1].strip()
            scndanstext = text(posanswers[1].strip(), BLK, scndans.xcoord, scndans.ycoord, scndans.xsize, scndans.ysize)
            trdans = buttons(580, 500 ,199 ,50, LGRY, GRY,0)
            thirdans = posanswers[2].strip()
            trdanstext = text(posanswers[2].strip(), BLK, trdans.xcoord, trdans.ycoord, trdans.xsize, trdans.ysize)
            frstans.button()
            frstanstext.showbtext()
            scndans.button()
            scndanstext.showbtext()
            trdans.button()
            trdanstext.showbtext()
            
            draw_score()
            pygame.display.update()
            clock.tick(15)

            
            
    

    
level1 = levels( "Karostas Cietums", "Karostas cietums jeb virssardze. Ēka celta ", "ap 1900. gadu un līdz pat 1997. gadam kalpojusi","kā militārpersonu disciplinārsodu izciešanas vieta.", "Cietums, no kura neviens nekad nav izbēdzis.",0 ,2 ,1)
level2 = levels( "Sv. Trīsvienības katedrāle", "Katedrāle atrodas uz Lielās ielas. Tās pamatakmens ","likts 1742. gadā un iesvētīta 1758. gadā. Celtniecība ", "pilnībā pabeigta 1866. gadā. Katedrāle ir bijusi lieciniece ", "svarīgam Somijas valsts neatkarības notikumam.",4 ,6, 5)
level3 = levels( "Lielais dzintars", "Nacionālas un Eiropas nozīmes daudzfunkcionāls","mākslas centrs. Tā tika celta divu gadu laikā no 2013. ", "līdz 2015. Ēku projektēja Austriešu arhitekts Folkers ", "Gīnke. Mājvieta Liepājas Simfoniskajam orķestrim.",8 ,10, 9)
level4 = levels( "Sv. Nikolaja Jūras katedrāle", "Karostas vizuālā un garīgā dominante. Katedrāles ","celtniecība sākās 1901. gadā. Tās pamatakmens ", "svinīgajā iesvētīšanas ceremonijā piedalījās arī ", "Krievijas cars Nikolajs II ar ģimeni.",12, 14, 13)
level5 = levels( "Liepājas Muzejs", "1924. gada 8. pamatskolas ēku atvēlēja muzeja ","iekārtošanai. Kopš 1935. gada ēkā atrodas pilsētas ", "muzejs. Izcils 20. gadsimta sākuma Liepājas ", "eklektisma arhitektūras paraugs.",16 ,18, 17)
level6 = levels( "Spoku Koks", "Veltīts latviešu leģendārajai rokgrupai “Līvi”.","“Spoku Koks” ir iespaidīgs sešus metrus augsts koks", ", kas veidots no četriem tūkstošiem metāla stienīšu. ", "Diennakts tumšajā laikā “Spoku koks” ir izgaismots.",20 ,22, 21)
level7 = levels( "Romas Dārzs", "Veidota 19. gadsimtā kā tirdzniecības pasāža","ar plašu un romantisku iekšpagalmu. Šobrīd ēkā ", "atrodas viesnīca, beķereja, biroji un veikali, bet ēkas ", "pazemes tuneļos ierīkota mākslas galerija ar veikalu.",24 ,26, 25)
level8 = levels( "Kārļa Zāles piemineklis", "1989.gadā saistībā ar tēlnieka Kārļa Zāles ","100. dzimšanas dienu pilsēta izsludināja pieminekļa ", "projektu konkursu. Par godu Latvijas valsts simtgadei", "un tēlnieka 130 gadu jubilejai piemineklis tika pabeigts.",28 ,30, 29)
level9 = levels( "Sv. Jāzepa katedrāle", "Lielākais katoļu dievnams Kurzemē ar bagātīgu ","un greznu interjeru. Katedrāles vēsture sākās 1747. gadā,", "kad šajā vietā uzcēla nelielu mūra baznīcu. Baznīcas ", "tornī ir ierīkota neliela izstāžu zāle.",32 ,34, 33)
level10 = levels( "Liepājas himnas tēlu skulptūras", "Vairākas skulptūras ar himnas tēliem veidoti no bronzas,","kas izvietoti pa visu Kurmājas prospekta garumu.", "Pie katra tēla var atrast vienu himnas pantiņu. Ejot ", "garām Liepājas vārnai, neaizmirsti paberzēt tās knābi. ;)",36 ,38, 37)
# Iziet no spēles
title_screen()
game_loop()
pygame.quit()
quit()
