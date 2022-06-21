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
        arr = []
        for i in range(0, 10):
            arr.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])

        arr[9][9] = "X"

        # Set obstacles
        # [row][column]
        arr[7][9] = "#"
        arr[7][8] = "#"
        arr[7][7] = "#"
        arr[8][7] = "#"

        return arr

    def printGrid(self):
        """
        Print the grid to the console.
        """
        for row in self.grid:
            print(row)

    def findPath(self):
        """
        Finds a path to the destination.
        :return: path, number of steps
        """
        totalSteps = 0
        path = []

        directions = [ [-1, -1], [0, -1], [1, -1],
                       [-1, 0], [1, 0],
                       [-1, 1], [0, 1], [1, 1]]
        queue = []
        queue.append(self.startingPoint) # starting point is (0,0)

        while len(queue) > 0:
            p = queue[0]
            queue.pop(0)

            # Check if at destination
            if p == self.endPoint:
                print("Found")
                return path, totalSteps

            # Mark the position as visited
            self.grid[p[0]][p[1]] = "+"

            # Check all 8 directions
            for i in range(8):
                a = p[0] + directions[i][0]
                b = p[1] + directions[i][1]

                # if the position is valid, add it to the queue
                if (a >= 0 and b >= 0 and a <= 9 and b <= 9) and (self.grid[a][b] == "-" or self.grid[a][b] == "X"):
                    queue.append((a, b))

        print("NOT found")
        return None, None


# ---------- Main ----------
pathfinder = PathFinder()
print("Starting grid:")
pathfinder.printGrid()
path, totalSteps = pathfinder.findPath()
print("End grid:")
pathfinder.printGrid()
