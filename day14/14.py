from timeit import default_timer as timer
from copy import deepcopy

def get_input():
    with open("./day14/14.in","r") as f:
         return [line.strip() for line in f.readlines()]

def p1(data):
    memory = dict()
    valueess = ''
    mask = 'x' * 32
    for line in data:
        cmd, val = line.split(' = ')
        if cmd == 'mask':
            mask = val
        else:
            valueess = cmd.lstrip('mem[').rstrip(']')
            val = bin(int(val))[2:].zfill(36)
            memory[valueess] = int(demask(val, mask))
    return sum([val for val in memory.values()])

def demask(value, mask):
    value = list(value)
    for i, maskVal in enumerate(mask):
        if maskVal != 'X':
            value[i] = maskVal 
    return int("".join(value), 2)

def p2(data):
    memory = dict()
    address = ''
    mask = 'x' * 32
    for line in data:
        cmd, val = line.split(' = ')
        if cmd == 'mask':
            mask = val 
        else:
            address = cmd.lstrip('mem[').rstrip(']')
            address = bin(int(address))[2:].zfill(36)
            # val = bin(int(val))[2:].zfill(36)
            for a in memoryDecoder(address, mask):
                memory[a] = int(val)
    return sum([val for val in memory.values()])

def memoryDecoder(value, mask):
    value = list(value)
    floating = 0
    for i, maskVal in enumerate(mask):
        if maskVal == '1':
            value[i] = maskVal
        if maskVal == 'X':
            value[i] = 'X'
            floating += 1
    
    addresses = [value]
    for i in range(floating):
        new_addreses = []
        for addr in addresses:
            next_X = next(i for i, c in enumerate(addr) if c == 'X')
            new_addreses.append("".join(addr[:next_X]) + '1' + "".join(addr[next_X+1:]))
            new_addreses.append("".join(addr[:next_X]) + '0' + "".join(addr[next_X+1:]))
        addresses = new_addreses
    return ["".join(addr) for addr in addresses]
    

print("Day 14: Docking Data")
data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")