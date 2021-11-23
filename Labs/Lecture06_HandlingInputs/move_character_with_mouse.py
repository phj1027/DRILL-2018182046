import random
from pico2d import *



KPU_WIDTH, KPU_HEIGHT = 883, 707


def handle_events():
    global running
    global dir
    global state

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                state = 2
            elif event.key == SDLK_LEFT:
                dir += 1
                state = 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND_small.png')
character = load_image('animation_sheet.png')

arrow = load_image('hand_arrow.png')

cx, cy = random.randint(KPU_WIDTH, 0), random.randint(0, KPU_HEIGHT)
frame = 0


dir = 0   # -1 left , +1 right
state = 0


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(cx, cy)


    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    delay(0.01)
close_canvas()















