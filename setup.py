from ia.bot import Bot
from random import choice
import time


def play(repeat=1, grid=None, random=False):
    if grid is None:
        if random:
            last_grids = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
            for i in range(repeat):
                x = choice(last_grids)
                last_grids.remove(x)

                robo = Bot(int(x))
                if i == 0:
                    time.sleep(10)
                robo.display_path_to_princess()

        else:
            for i in range(repeat):
                robo = Bot(i)
                robo.display_path_to_princess()
    else:
        robo = Bot(grid)
        robo.display_path_to_princess()


if __name__ == '__main__':
    play(repeat=12, random=True)
