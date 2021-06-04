from collections import defaultdict


class FireTruck:
    def __init__(self):
        self.streetGraph = defaultdict(list)
        self.goal = 0
        self.paths = []

    def printPath(path):
        for index, node in enumerate(path):
            print(node, end=' ')
            if index == len(path) - 1:
                print()

    def addEdge(self, u, v):
        self.streetGraph[u].append(v)
        self.streetGraph[v].append(u)

    def dfs(self, v, visited):
        visited.append(v)

        if v == self.goal:
            self.paths.append(visited)
            FireTruck.printPath(visited)
            visited.pop()
            return

        for neighbour in self.streetGraph[v]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

        visited.pop()

    def findAllPaths(self, start, goal):
        visited = []
        visited.append(start)
        self.goal = goal
        for neighbour in self.streetGraph[start]:
            self.dfs(neighbour, visited)


def main():
    with open('input.txt', 'r') as inputFile:
        lines = inputFile.readlines()

        fireTruck = FireTruck()
        case, goal = 0, 0
        for line in lines:
            line = line.strip().split(' ')
            if len(line) == 1:
                goal = int(line[0])
                case += 1
            elif len(line) == 2 and int(line[0]) != 0 and int(line[1]) != 0:
                u, v = line
                fireTruck.addEdge(int(u), int(v))
            else:
                print(f'CASE {case}:')
                fireTruck.findAllPaths(1, goal)
                print(
                    f'There are {len(fireTruck.paths)} routes from the firestation to streetcorner {fireTruck.goal}')
                fireTruck = FireTruck()


if __name__ == '__main__':
    main()
