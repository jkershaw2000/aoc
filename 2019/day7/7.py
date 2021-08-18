import computer
from itertools import permutations
def get_input():
    with open("7.in", "r") as f:
        return [int(val) for val in f.read().split(",")]

program = get_input()
outputs = []
for perm in permutations(range(5), 5):
    out = 0
    for phase in perm:
        out = computer.intcode_computer(program, phase, out)
        program = get_input()
    outputs.append(out)
    out = 0
print(max(outputs))


        