import pygame
import time
# from Bot import Bot


class GameBoard:
    def __init__(self):#, grid):
        self.screen = pygame.display.set_mode((650, 490))
        self.mario = pygame.image.load('mario.jpg')
        self.peach = pygame.image.load('peach.jpg')
        self.background = pygame.image.load('background2.jpg')
        # self.bot = Bot(grid)
        self.set_position()
        self.update()
        # self.bot.display_path_to_princess()
        # self.move()

    def set_position(self, mario_h=4, mario_v=5):
        self.mario_pos = (mario_h, mario_v)
        self.peach_pos = self.get_peach_pos()

    def update(self):
        self.screen.blit(self.background, (2, 2))
        self.screen.blit(self.peach, self.peach_pos)
        self.screen.blit(self.mario, self.mario_pos)
        pygame.display.flip()

    def move(self, mov):
        # for up in range(self.bot.get_movements()['UP']):
        if mov == 'UP':
            self.mario_pos = (self.mario_pos[0], self.mario_pos[1] - 40)
            self.update()
            time.sleep(1)

        # for down in range(self.bot.get_movements()['DOWN']):
        if mov == 'DOWN':
            self.mario_pos = (self.mario_pos[0], self.mario_pos[1] + 40)
            self.update()
            time.sleep(1)

        # for right in range(self.bot.get_movements()['RIGHT']):
        if mov == 'RIGHT':
            self.mario_pos = (self.mario_pos[0] + 40, self.mario_pos[1])
            self.update()
            time.sleep(1)

        # for left in range(self.bot.get_movements()['LEFT']):
        if mov == 'LEFT':
            self.mario_pos = (self.mario_pos[0] - 40, self.mario_pos[1])
            self.update()
            time.sleep(1)

    def get_peach_pos(self):
        p_v_index = self.find_peach_v_pos()
        p_h_index = self.find_peach_h_pos(p_v_index)

        return p_h_index * 40 - 32, p_v_index * 40 - 32

    def find_peach_v_pos(self):
        p_index = 0
        grid=['-----', '--m--', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '----p']
        for i in grid:
            if "p" in i:
                return p_index

            p_index += 1

    def find_peach_h_pos(self, v_pos):
        p_index = 0
        grid = ['-----', '--m--', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '----p']
        for b in grid[v_pos]:
            if "p" in b:
                return p_index

            p_index += 1


# GameBoard(grid=['-----', '--m--', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '----p'])
