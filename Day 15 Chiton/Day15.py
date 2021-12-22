import sys
import heapq

# https://www.redblobgames.com/pathfinding/a-star/implementation.html#python-dijkstra
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def dijkstras(grid, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {start: 0}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in get_neighbours(current, grid):
            new_cost = cost_so_far[current] + grid[current[0]][current[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def get_neighbours(node, grid):
    neighbours = []

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        adj_x = node[0] + dx
        adj_y = node[1] + dy

        if in_range(adj_x, adj_y, grid):
            neighbours.append((adj_x, adj_y))

    return neighbours


def in_range(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])


def part_one(grid):
    dijkstras(grid, (0, 0), (len(grid)-1, len(grid)-1))

    came_from, cost_so_far = dijkstras(grid, (0, 0),  (len(grid)-1, len(grid)-1))
    path = reconstruct_path(came_from, (0, 0), (len(grid)-1, len(grid)-1))

    risk = 0
    for node in path:
        x, y = node

        if not node == (0, 0):
            risk += grid[x][y]

    print("Risk:", risk)


def part_two(grid):
    new_size = len(grid) * 5
    new_grid = [[0 for _ in range(new_size)] for _ in range(new_size)]

    for x in range(new_size):
        for y in range(new_size):
            old_x, old_y = x % len(grid), y % len(grid)
            magnitude = x // len(grid) + y // len(grid)
            new_value = (grid[old_x][old_y] + magnitude)
            new_grid[x][y] = new_value if new_value <= 9 else new_value % 9

    came_from, cost_so_far = dijkstras(new_grid, (0, 0), (new_size-1, new_size-1))
    path = reconstruct_path(came_from, (0, 0), (new_size-1, new_size-1))

    risk = 0
    for node in path:
        x, y = node

        if not node == (0, 0):
            risk += new_grid[x][y]

    print("Risk:", risk)


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return path


def main():
    file = open("input.txt", "r")
    grid = [[int(risk) for risk in row] for row in file.read().split('\n')]

    part_one(grid)
    part_two(grid)


if __name__ == "__main__":
    main()
