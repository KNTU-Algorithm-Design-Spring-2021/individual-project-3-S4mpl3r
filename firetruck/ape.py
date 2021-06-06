from collections import defaultdict
import random


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

    def isPromising(self, v, visited):
        return v not in visited

    def dfs(self, v, visited):
        visited.append(v)

        if v == self.goal:
            self.paths.append(visited)
            FireTruck.printPath(visited)
            visited.pop()
            return

        for neighbour in self.streetGraph[v]:
            if self.isPromising(neighbour, visited):
                self.dfs(neighbour, visited)

        visited.pop()

    def findAllPaths(self, start, goal):
        visited = []
        visited.append(start)
        self.goal = goal
        for neighbour in self.streetGraph[start]:
            self.dfs(neighbour, visited)

    def estimateComplexity(self, runs):
        sum = 0
        for _ in range(runs):
            sum += self.estimate(1)

        return sum / runs

    def estimate(self, start):
        v = start
        visited = [v]
        numnodes, m, mprod = 1, 1, 1
        while m != 0:
            t = len(self.streetGraph[v])
            mprod = mprod * m
            numnodes = numnodes + mprod*t
            promisings = []
            for neighbor in self.streetGraph[v]:
                if self.isPromising(neighbor, visited):
                    promisings.append(neighbor)
            m = len(promisings)
            if m != 0:
                v = promisings[int(random.random() *
                                   len(promisings))]
                visited.append(v)

        return numnodes


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
                # print(f'estimation: {fireTruck.estimateComplexity(10000)}')
                print(
                    f'There are {len(fireTruck.paths)} routes from the firestation to streetcorner {fireTruck.goal}')
                fireTruck = FireTruck()


if __name__ == '__main__':
    main()
