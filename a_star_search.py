import heapq
import random
import numpy as np

# -------------------------------------------------------------------------------------------------------------------- #
# Used:                                                                                                                #
# https://www.analytics-link.com/post/2018/09/14/applying-the-a-path-finding-algorithm-in-python-part-1-2d-square-grid #
# ---------------------------------------------------------------------------------------------------------------------#

class PathFinder:
    def __init__(self):
        self.grid = self.buildGrid()
        self.startingPoint = (0,0)
        self.endPoint = (9,9)

    def buildGrid(self):
        """
        Build a 10x10 grid.
        :return: a 10x10 array
        """
        arr = np.zeros([10,10])
        # Set obstacles
        # [row][column]
        arr[7][9] = 1
        arr[7][8] = 1
        arr[7][7] = 1
        arr[8][7] = 1
        return arr

    def printGrid(self):
        """
        Print the grid to the console.
        """
        grid_as_list = self.grid.astype(int).tolist()

        grid_as_list[self.startingPoint[0]][self.startingPoint[1]] = "S"
        grid_as_list[self.endPoint[0]][self.endPoint[0]] = "E"

        for i in range(0,len(grid_as_list)):
            for j in range(0, len(grid_as_list[i])):
                if grid_as_list[i][j] == 0:
                    grid_as_list[i][j] = "-"
                if grid_as_list[i][j] == 2:
                    grid_as_list[i][j] = "+"
                if grid_as_list[i][j] == 1:
                    grid_as_list[i][j] = "#"

        for i in grid_as_list:
            print(i)

    def plotPath(self, data):
        for i,j in data:
            self.grid[i][j] = 2

    def addObstacles(self):
        # Add 20 random obstacles and print their location
        obstacles = []
        while len(obstacles) < 20:
            row = random.randint(0,9)
            col = random.randint(0,9)
            if self.grid[row,col] == 0:
                self.grid[row, col] = 1
                obstacles.append((col, row))
        print('Obstacles at:', obstacles)

    def heuristic(self, a, b):
        # Straight lines as heuristic given we can travel diagonally
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def findPath(self):
        directions = [ [-1, -1], [0, -1], [1, -1],
                       [-1, 0], [1, 0],
                       [-1, 1], [0, 1], [1, 1]]

        close_set = set() # positions that do not need to be revisited
        came_from = {} # dictonary that contains the route paths we took in each iteration.
        gscore = {self.startingPoint: 0} # dictonary containing G scores by iteration
        fscore = {self.startingPoint: self.heuristic(self.startingPoint, self.endPoint)} # dictonary containing F scores by iteration
        oheap = [] # open list, containing all positions that are being considered to find shortest path
        heapq.heappush(oheap, (fscore[self.startingPoint], self.startingPoint))

        # continuing looping until there are no options left
        while oheap:
            current = heapq.heappop(oheap)[1]
            if current == self.endPoint:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                self.plotPath(data)
                return data

            close_set.add(current)

            for i, j in directions:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)

                if 0 <= neighbor[0] < self.grid.shape[0]:
                    if 0 <= neighbor[1] < self.grid.shape[1]:
                        if self.grid[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, self.endPoint)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))


# ---------- Main ---------- #
pathfinder = PathFinder()
print("Starting...")
pathfinder.printGrid()
print("\n")

print("Adding obstacles...")
pathfinder.addObstacles()
print("\n")

path = pathfinder.findPath()
pathfinder.printGrid()
if path == None:
    print("Unable to reach delivery point")
else:
    print("Complete.")
    path.reverse()
    print('\nPath:', path)
    totalSteps = str(len(path))
    print("Total steps: " + totalSteps)

