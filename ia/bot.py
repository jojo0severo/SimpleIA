from board.game import GameBoard


class Bot:
    def __init__(self, grid):
        self.board = GameBoard(grid)

    def display_path_to_princess(self):
        p_v_index = self.board.find_peach_v_pos()
        p_h_index = self.board.find_peach_h_pos(p_v_index)

        m_v_index = self.board.find_mario_v_pos()
        m_h_index = self.board.find_mario_h_pos(m_v_index)

        while m_v_index > p_v_index:
            self.board.move('UP')
            m_v_index -= 1

        while m_v_index < p_v_index:
            self.board.move('DOWN')
            m_v_index += 1

        while m_h_index > p_h_index:
            self.board.move('LEFT')
            m_h_index -= 1

        while m_h_index < p_h_index:
            self.board.move('RIGHT')
            m_h_index += 1
