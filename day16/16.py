from timeit import default_timer as timer
from numpy import prod
def get_input():
    with open("./day16/test.in", "r") as f:
        fields, own, others = f.read().split("\n\n")
    fields = [[f.split(' or ')for f in field.split(': ')]
              for field in fields.split("\n")]
    rules = {}
    for item in fields:
        a = set()
        for val in item[1]:
            val = val.split('-')
            a |= set(range(int(val[0]), int(val[1])+1))
        rules[item[0][0]] = a 
    own = list(map(int, own.splitlines()[1].split(',')))
    others = [list(map(int, other.split(','))) for other in others.splitlines()[1:]]
    return (rules, own, others)


def p1(data):
    res = 0
    # Aid with part2
    valid = []
    for ticket in data[2]:
        # Aid with part2
        invalid = False
        for value in ticket:
            if not any([value in field for field in data[0].values()]):
                invalid = True
                res += value
        # Aid with part2
        if not invalid:
            valid.append(ticket)
    return res, valid


def p2(data, tickets):
    rules = data[0]
    own = data[1]
    # Dictionary of what field relates to what number
    rulesIndex = {key: -1 for key in rules.keys()}
    for ticket in tickets:
        for name, check in rules.items():
            if all(val in check for val in ticket):
                pass
    

    ans = 1
    for key, val in rulesIndex.items():
        if "departure" in val:
            ans *= own[rulesIndex[key]]
    return ans


print("Day 16: Ticket Translation")
data = get_input()
p1start = timer()
p1, tickets = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")

p2start = timer()
p2 = p2(data, tickets)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")
