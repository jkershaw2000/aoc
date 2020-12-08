from timeit import default_timer as timer

def get_input():
    with open("./day8/8.in","r") as f:
        return [line.strip() for line in f.readlines()]

def run(instructions):
    pc, acc = 0, 0
    seen = [False] * len(instructions)
    while pc < len(instructions) and not seen[pc]:
        seen[pc] = True
        cmd, val = instructions[pc][:3], instructions[pc][4:]
        pc += 1
        if cmd == "acc": acc += int(val)
        elif cmd == "jmp": pc += int(val) -1 # pc already incremented by 1
    return acc, seen, pc

def p2(seen):
    swap = {'nop':'jmp', 'jmp':'nop'}
    for i, used in enumerate(seen):
        instructions = get_input()
        cmd, val = instructions[i][:3], instructions[i][4:]
        if used == True and cmd in ['nop', 'jmp']:
            instructions[i] = swap[cmd] + val
        acc, _, pc = run(instructions)
        if  pc ==  len(instructions):
            return acc


            


print("Day 8: Handheld Halting")

p1start = timer()
p1, seen, _ = run(get_input())
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(seen)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")