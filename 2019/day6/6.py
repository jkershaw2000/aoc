from os import walk


def get_input():
    with open("6.test", "r") as f:
        return [line.split(")") for line in f.read().splitlines()]

# Each pair (X, Y) means Y orbits X
orbits = get_input()
graph = {}
for pair in orbits:
    if pair[0] not in orbits:
        graph[pair[0]] = []
    graph[pair[0]].append(pair[1])

def walkOrbits(i):
    ans = 0
    for v in graph.get(i, []):
        ans += walkOrbits(v) + 1
    return ans

ans = 0
for i in graph:
    ans += walkOrbits(i)

print(ans)

