from timeit import default_timer as timer
from typing import DefaultDict

def get_input():
    with open("./day19/test.in","r") as f:
        rules, messages= f.read().split("\n\n")
    r = DefaultDict(list)
    for rule in rules.split("\n"):
        name, expr = rule.split(': ')
        for e in expr.split("|"):
            if e[0] == '"':
                r[int(name)] = e[1]
            else:
                r[int(name)].append([int(el) for el in e if el != ' '])
    return r, messages

def p1():
    res = 0
    for msg in messages:
        # Matching to rule 0 for question
        # Using a stacks so reverse
        if check(msg, list(reversed(rules[0][0]))):
            res += 1
    return res

def check(s, stack):
    # Tail recursion
    #  Base Cases
    if len(stack) > len(s):
        return False
    elif len(stack) == 0 or len(s) == 0:
        return len(stack) == 0 and len(s) == 0
    
    el = stack.pop()
    # Must be str to remove something from msg
    if isinstance(el, str):
        if s[0] == el:
            return check(s[1:], stack.copy())
    else:
        for rule in rules[int(el)]:
            if check(s, stack + list(reversed(rule))):
                return True
    return False


def p2(rules, msgs):
    pass

print("Day 19: Monster Messages")
rules, messages = get_input()
p1start = timer()
print(rules)
p1 = p1()
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")
p2start = timer()
p2 = p2(rules, messages)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")