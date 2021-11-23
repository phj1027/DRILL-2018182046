from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball21:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(1, 799), 599
        self.fy = random.randint(1, 30)


    def update(self):


    def draw(self):
        self.image.draw(self.x, self.y)

class Ball41:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(1, 799), 599
        self.fy = y = random.randint(1, 30)


    def update(self):
        self.y >= 70:
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

grass = Grass()
boy = Boy()

running = True



ix21 = random.randint(1, 20)


team = [Boy() for i in range(11)]
ball21 = [Ball21() for i in range(idx21)]



while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for ball in ball21:
        ball.update()
    for ball in ball41:
        ball.update()


    update_canvas()

    delay(0.05)





close_canvas()