import time

class SokoBot:
    def __init__(self):
        self.player = None
        self.crates = set()
        self.goals = set()
        self.walls = set()
        self.board = None
        self.state = None
        self.width = None
        self.height = None

    def solveSokobanPuzzle(self, width, height, mapData, itemsData):
        
        self.board = Board(width, height, mapData, itemsData)
        
        self.player = self.board.player
        self.crates = self.board.crates
        self.goals = self.board.goals
        self.walls = self.board.walls
        self.width = width
        self.height = height

        self.state = State(self)

        print("Player: " + str(self.player))
        print("Crates: " + str(self.crates))
        print("Goals: " + str(self.goals))

        self.state.heuristic()

        currentState = (self.player, self.crates)
        
        actions = self.state.nextState(currentState)
        print("Possible next states:", actions)
        return ""

class Board:
    def __init__(self, width, height, map_data, items_data):
        self.width = width
        self.height = height
        self.state = None
        self.walls = set()
        self.goals = set()
        self.player = None
        self.crates = set()

        for i in range(height):
            for j in range(width):
                if map_data[i][j] == '#':
                    self.walls.add((i, j))
                if (map_data[i][j] == '.'):
                    self.goals.add((i, j))
                if (items_data[i][j] == '@'):
                    self.player = (i, j)
                if (items_data[i][j] == '$'):
                    self.crates.add((i, j))

        self.state = (self.player, self.crates)

class State:
    def __init__(self, board):
        self.player = board.player
        self.crates = board.crates
        self.goals = board.goals
        self.walls = board.walls
        self.width = board.width
        self.height = board.height

    def heuristic(self):
        playerToCrates = dict()
        cratesToGoals = dict()

        for i in self.crates:
            playerToCrates[i] = self.get_distance(self.player, i)

        if playerToCrates:
            print("Player to Boxes Distance: " + str(playerToCrates))
            print("Minimum Player to Crate Distance:", str(min(playerToCrates.values())))

        for i in self.crates:
            for j in self.goals:
                cratesToGoals[i, j] = self.get_distance(i, j)

        if playerToCrates:
            print("Boxes to Goals Distance: ", str(cratesToGoals))
            print("Minumum Player to Box Distance: " + str(min(playerToCrates.values())))

        return 0

    def get_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def allCratesOnGoals(self, state):
        player, crates = state
        return crates == self.goals

    def nextState(self, state):
        player, crates = state
        player_row, player_col = player
        nextStates = []

        actions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r, c in actions:
            newPlayerPos = (player_row + r, player_col + c)
            newPlayerRow, newPlayerCol = newPlayerPos

            if newPlayerPos in self.walls:
                continue
            
            if newPlayerPos in crates:
                newCratesPos = (newPlayerRow + r, newPlayerCol + c)

                if newCratesPos in self.walls or newCratesPos in crates:
                    continue
                
                updatedCrates = (crates - {newPlayerPos}) | {newCratesPos}
                nextStates.append((newPlayerPos, updatedCrates))

            else:
                nextStates.append((newPlayerPos, crates))
        return nextStates
