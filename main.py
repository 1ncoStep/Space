import time
from sprite import *


def dialogue_mode(sprite, text):
    sprite.update()
    screen.blit(sprite.image, sprite.rect)

    text1 = f1.render(start_text[text_number], True, 'white')
    screen.blit(text1, (280, 450))

    if text_number < len(start_text) - 1:
        text2 = f1.render(start_text[text_number + 1], True, 'white')
        screen.blit(text2, (280, 475))


pg.init()
pg.mixer.init()

size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Космические коты")

FPS = 120
clock = pg.time.Clock()

is_running = True
mode = "start_scene"

meteorites = pg.sprite.Group()
mice = pg.sprite.Group()
lasers = pg.sprite.Group()
back = pg.image.load('фон.png')
back = pg.transform.scale(back, (size[0], size[1]))
text_number = 0
f1 = pg.font.Font('Космические коты - шрифт.otf', 25)
captain = Captain()
alien = Alien()
starship = Starship()
heart = pg.image.load('сердце.png').convert_alpha()
heart30x30 = pg.transform.scale(heart, (30, 30))
hp_counter = 3

start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]

alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]

final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки.",
              "",
              ""]


while is_running:
    screen.blit(back, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

        if event.type == pg.KEYDOWN:
            if mode == 'start_scene' or mode == 'alien_scene':
                text_number += 2

                if text_number > len(alien_text):
                    text_number = 0
                    mode = 'meteorites'
                    start_time = time.time()

            if mode == "alien_scene":
                text_number += 2

                if text_number > len(alien_text):
                    text_number = 0
                    hp_counter = 3
                    mode = 'moon'
                    start_time = time.time()

            if mode == "final_scene":
                text_number += 2

                if text_number > len(alien_text):
                    text_number = 0
                    mode = 'end'

        if event.type == pg.MOUSEBUTTONDOWN:
            if mode == 'moon':
                if event.button == 1:
                    lasers.add(Laser(starship.rect.midtop))

    if mode == "start_scene":
        dialogue_mode(captain, start_text)
        
    if mode == "meteorites":
        if time.time() - start_time >= 5.0:
            mode = 'alien_scene'

        if random.randint(1, 30) == 1:
            meteorites.add(Meteorite())

        starship.update()
        meteorites.update()

        hit = pg.sprite.spritecollide(starship, meteorites, True)
        for hits in hit:
            hp_counter -= 1

            if hp_counter <= 0:
                is_running = False

        for a in range(hp_counter):
            screen.blit(heart30x30, (a * 30, 0))

        screen.blit(starship.image, starship.rect)
        meteorites.draw(screen)

    if mode == "alien_scene":
        dialogue_mode(alien, alien_text)

    if mode == "moon":
        hp_counter = 3

        if time.time() - start_time >= 30.0:
            mode = 'final scene'

        if random.randint(1, 30) == 1:
            mice.add(Mouse_starship())

        starship.update()
        mice.update()
        lasers.update()

        hit = pg.sprite.spritecollide(starship, mice, True)
        for hits in hit:
            hp_counter -= 1

            if hp_counter <= 0:
                is_running = False

        hit = pg.sprite.spritecollide(lasers, mice, True, True)

        for a in range(hp_counter):
            screen.blit(heart30x30, (a * 30, 0))

        screen.blit(starship.image, starship.rect)
        mice.draw(screen)
        lasers.draw(screen)

    if mode == "final_scene":
        dialogue_mode(alien, alien_text)

    pg.display.flip()
    clock.tick(FPS)
