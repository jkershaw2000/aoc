import heapq
from collections import defaultdict

with open("2021/day15/15.in", "r") as f:
    data = [[int(l) for l in line.strip()] for line in f.readlines()]


def expand(grid):
    expanded = [[None for _ in range(len(grid) * 5)] for _ in range(len(grid) * 5)]

    for row in range(len(grid) * 5):
        for col in range(len(grid) * 5):
            copy = grid[row % len(grid)][col % len(grid)]
            offset = row // len(grid) + col // len(grid)
            risk = (copy + offset - 1) % 9 + 1
            expanded[row][col] = risk
    return expanded


class Graph:
    def __init__(self, data):
        self.number_of_vertices = len(data[0]) * len(data)
        self.edges = defaultdict(list)
        for i in range(len(data)):
            for j in range(len(data[0])):
                for (adj_i, adj_j) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if len(data) > adj_i >= 0 and len(data[0]) > adj_j >= 0:
                        neighbor_coords = (adj_i, adj_j)
                        neighbor_weight = data[adj_i][adj_j]
                        self.edges[(i, j)].append((neighbor_coords, neighbor_weight))

    def dijkstra(self, start):
        distances = {vertex: float("inf") for vertex in self.edges}
        distances[start] = 0
        visited = set()

        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (0, start))

        while pq:
            _, current_vertex = heapq.heappop(pq)
            visited.add(current_vertex)

            for neighbor in self.edges[current_vertex]:
                neighbor_coords, neighbor_dist = neighbor
                if neighbor[0] not in visited:
                    old = distances[neighbor_coords]
                    new = distances[current_vertex] + neighbor_dist
                    if new < old:
                        heapq.heappush(pq, (new, neighbor_coords))
                        distances[neighbor_coords] = new
        return distances


p1 = Graph(data)
start = (0, 0)
end = (len(data) - 1, len(data[0]) - 1)
part1 = p1.dijkstra(start)[end]
expanded_data = expand(data)
p2 = Graph(expanded_data)
end = (len(expanded_data) - 1, len(expanded_data[0]) - 1)
part2 = p2.dijkstra(start)[end]
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
