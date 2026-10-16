class SokoBot:
    def __init__(self):
        self.board = None

    def solveSokobanPuzzle(self, width, height, map_data, items_data):
        return ""

class Board:
    def __init__(self, width, height, map_data, items_data):
        self.state = None
        self.walls = set()
        self.goals = set()
        self.player = None
        self.crates = set()

        for i in height:
            for j in width:
                if map_data[i][j] == '#':
                    self.walls.add((i, j))
                if (map_data[i][j] == '.'):
                    self.goals.add((i, j))
                if (items_data[i][j] == '@'):
                    self.player = (i, j)
                if (items_data[i][j] == '#'):
                    self.crates.add((i, j))

        self.state = State(self, self.player, self.crates)

class State:
    DIRECTIONS = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def __init__(self, board, player, crates):
        self.board = board
        self.player = player
        self.crates = crates

    def get_successors(self):
        pass

    def heuristic(self):
        pass

    def get_distance(self, a, b):
        pass
