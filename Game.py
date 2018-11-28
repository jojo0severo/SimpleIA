import pygame
import time

mario = pygame.image.load('mario.jpg')
background = pygame.image.load('background.jpg')
mario_pos = (3, 3)

screen = pygame.display.set_mode((650, 490))


def displayPathtoPrincess(grid):
    global mario_pos

    time.sleep(3)
    p_v_index = find_peach_v_pos(grid)
    m_v_index = find_mario_v_pos(grid)

    m_h_index = find_mario_h_pos(grid, m_v_index)
    p_h_index = find_peach_h_pos(grid, p_v_index)

    mario_pos = (m_h_index, m_v_index)
    update()

    if m_v_index > p_v_index:
        while m_v_index > p_v_index:
            m_v_index -= 1
            mario_pos = (mario_pos[0], m_v_index * 20)
            update()
            time.sleep(1)
            print("UP")
    else:
        while m_v_index < p_v_index:
            m_v_index += 1
            mario_pos = (mario_pos[0], m_v_index * 20)
            update()
            time.sleep(1)
            print("DOWN")

    if m_h_index > p_h_index:
        while m_h_index > p_h_index:
            m_h_index -= 1
            mario_pos = (m_h_index * 20, mario_pos[1])
            update()
            time.sleep(1)
            print("LEFT")
    else:
        while m_h_index < p_h_index:
            m_h_index += 1
            mario_pos = (m_h_index * 20, mario_pos[1])
            update()
            time.sleep(1)
            print("RIGHT")


def find_peach_h_pos(grid, h_pos):
    p_index = 0
    for b in grid[h_pos]:
        if "p" in b:
            return p_index

        p_index += 1


def find_mario_h_pos(grid, h_pos):
    m_index = 0
    for b in grid[h_pos]:
        if "m" in b:
            return m_index

        m_index += 1


def find_peach_v_pos(grid):
    p_index = 0
    for i in grid:
        if "p" in i:
            return p_index

        p_index += 1


def find_mario_v_pos(grid):
    m_index = 0
    for line in grid:
        if "m" in line:
            return m_index

        m_index += 1


def update():
    screen.blit(background, (1, 1))
    screen.blit(mario, mario_pos)
    pygame.display.flip()


update()
time.sleep(2)
grid = ['-----', '--m--', '-----', '-----', '----p']
displayPathtoPrincess(grid)
time.sleep(10)
