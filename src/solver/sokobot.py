class SokoBot:
    def __init__(self):
        self.board = None

    def solveSokobanPuzzle(self, width, height, mapData, itemsData):
        self.board = Board(width, height, mapData, itemsData)

        # while self.board.state.heuristic() != 0:

        return ""

class Board:
    def __init__(self, width, height, map_data, items_data):
        self.walls = set()
        self.goals = set()

        crates = set()
        player = None

        self.state = None

        for i in range(height):
            for j in range(width):
                if map_data[i][j] == '#':
                    self.walls.add((i, j))
                if (map_data[i][j] == '.'):
                    self.goals.add((i, j))
                if (items_data[i][j] == '@'):
                    player = (i, j)
                if (items_data[i][j] == '$'):
                    crates.add((i, j))

        self.state = (self, player, crates)

class State:
    DIRECTIONS = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    )

    def __init__(self, board, player, crates):
        self.board = board
        self.player = player
        self.crates = crates

    def get_successors(self):
        successors = set()

        player_r, player_c = self.player

        for dir_r, dir_c in self.DIRECTIONS:
            next_player_position = (
                player_r + dir_r,
                player_c + dir_c,
            )

            if next_player_position in self.board.walls:
                continue

            new_crates_positions = set(self.crates)

            if next_player_position in self.crates:
                crate_r, crate_c = next_player_position

                next_crate_position = (
                    crate_r + dir_r,
                    crate_c + dir_c,
                )

                if (
                    next_crate_position in self.board.walls
                    or next_crate_position in self.crates
                ):
                    continue

                new_crates_positions.remove(next_player_position)
                new_crates_positions.add(next_crate_position)

            successors.add(
                State(
                    self.board,
                    next_player_position,
                    frozenset(new_crates_positions),
                )
            )

        return successors
