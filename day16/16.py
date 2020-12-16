from timeit import default_timer as timer

def get_input():
    with open("./day16/16.in", "r") as f:
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
    # Dictionary of what field relates to what column
    potentialRulesIndex = {key: [] for key in rules.keys()}
    rulesIndex = {key: None for key in rules.keys()}
    # Packs data up by column
    tickets = list(zip(*tickets))
    for values in tickets:
        # Go throigh and find what each 'column' could represent based on where it would be valid for all.
        for cond, nums in rules.items():
            if all(val in nums for val in values):
                potentialRulesIndex[cond].append(values)

    # Assumed always column with just one option
    while [None] * len(potentialRulesIndex.values()) !=  list(potentialRulesIndex.values()):
        for cond, poss in potentialRulesIndex.items():
            removed = None
            if poss != None:
                # Only option that the column can be
                if len(poss) == 1:
                    rulesIndex[cond] = poss[0]
                    potentialRulesIndex[cond] = None
                    removed = poss
                # If found column with 1 item, remove all referces to it from other potential rules.
                if removed != None :
                    for c in potentialRulesIndex.keys():
                        if potentialRulesIndex[c] != None and removed[0] in potentialRulesIndex[c]:
                            potentialRulesIndex[c].remove(removed[0])

    ans = 1
    for key, val in rulesIndex.items():
        index = tickets.index(val)
        if "departure" in key:
            ans *= own[index]
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
