from timeit import default_timer as timer
from sympy.ntheory.modular import crt

def get_input():
    with open("./day13/13.in","r") as f:
        data = f.readlines()
    return int(data[0]), data[1].split(',')

def p1(data):
    # Chinnese Remainder Theoem 
    earliest = data[0]
    busses = {int(bus):earliest for bus in data[1] if bus != 'x'}
    for bus in busses.keys():
        busses[bus] = (earliest - (earliest % bus)) + bus
    res = [(item[0], item[1]) for item in busses.items() if item[1] == min(busses.values())]
    return res[0][0] * (res[0][1] - earliest)


        
def p2(data):
    offsets = [int(bus)-key for key, bus in enumerate(data[1]) if bus != 'x']
    bussses = [int(bus) for _ ,bus in enumerate(data[1]) if bus!= 'x']
    return crt(bussses, offsets) [0]
print("Day 13: Shuttle Search")


data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")
