import time


class SokoBot:
    def __init__(self):
        self.player = None
        self.crates = set()
        self.goals = set()

    def solveSokobanPuzzle(self, width, height, mapData, itemsData):
        self.initialize(width, height, mapData, itemsData)

        print("Player: " + str(self.player))
        print("Crates: " + str(self.crates))
        print("Goals: " + str(self.goals))

        self.heuristic()

        return ""

    def initialize(self, width, height, mapData, itemsData):
        self.player = ()
        for i in range(height):
            for j in range(width):
                print(itemsData[i][j], end="")
                if mapData[i][j] == '.':
                    self.goals.add((i, j))
                if itemsData[i][j] == '$':
                    self.crates.add((i, j))
                if itemsData[i][j] == '@':
                    self.player = (i, j)
            print()

    def heuristic(self):
        playerToCrates = dict()
        createsToGoal = dict()

        for i in self.crates:
            playerToCrates[i] = self.get_distance(self.player, i)

        print("Player to Boxes Distance: " + str(playerToCrates))
        print("Minumum Player to Box Distance: " + str(min(playerToCrates, key=playerToCrates.get)))

        for i in self.crates:
            for j in self.goals:
                createsToGoal[i, j] = self.get_distance(i, j)

        print("Boxes to Goals Distance: " + str(createsToGoal))
        print("Minumum Box to Goal Distance: " + str(min(createsToGoal, key=createsToGoal.get)))

        return 0

    def get_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
