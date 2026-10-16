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

        self.state = State(self.player, self.crates, self)


class State:
    def __init__(self, board, player, crates):
        self.board = board
        self.player = player
        self.crates = frozenset(crates)

    def heuristic(self):
        if not self.crates or not self.board.goals:
            return 0

        player_to_crate = min(
            self.distance(self.player, crate)
            for crate in self.crates
        )

        crate_to_goal = min(
            self.distance(crate, goal)
            for crate in self.crates
            for goal in self.board.goals
        )

        return player_to_crate + crate_to_goal

    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_successors(self):
        successors = []

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            next_player = (
                self.player[0] + dr,
                self.player[1] + dc
            )

            if next_player in self.board.walls:
                continue

            next_crates = set(self.crates)

            if next_player in self.crates:
                next_crate = (
                    next_player[0] + dr,
                    next_player[1] + dc
                )

                if next_crate in self.board.walls:
                    continue

                if next_crate in self.crates:
                    continue

                next_crates.remove(next_player)
                next_crates.add(next_crate)

            successors.append(
                State(next_player, next_crates, self.board)
            )

        return successors

    def from_raw(width, height, map_data, items_data):
        for
