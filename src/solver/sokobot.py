class SokoBot:
    def __init__(self):
        self.board = None

    def solveSokobanPuzzle(self, width, height, mapData, itemsData):
        self.board = Board(width, height, mapData, itemsData)

        currentMoves = 0
        maxMoves = 100

        while self.heuristic(self.board.state) != 0 and currentMoves < maxMoves:
            # select next state
            maxMoves += 1
            break

        return ""

    def heuristic(self, state):
        unresolved_crates = state.crates - state.board.goals

        component1 = self.closest_crate_to_player(state.player, unresolved_crates)
        component2 = self.closest_goal_to_crate(unresolved_crates, state.board.goals)

        return component1 + component2 - 1

    def closest_crate_to_player(self, player, crates):
        return min(self.distance(player, crate) for crate in crates)

    def closest_goal_to_crate(self, crates, goals):
        return min(self.distance(crate, goal) for crate in crates for goal in goals)

    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

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

        self.state = State(self, player, frozenset(crates))

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

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented

        return (
            self.player == other.player
            and self.crates == other.crates
        )

    def __hash__(self):
        return hash((self.player, self.crates))
