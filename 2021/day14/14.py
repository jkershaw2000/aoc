from collections import Counter

with open("2021/day14/14.in", "r") as f:
    start = f.readline().strip()
    rules = [line.strip().split(" -> ")for line in f.readlines()[1:]]
    rules  = {rule[0]: rule[1] for rule in rules}

def solve(start, rules, ITERATIONS=10):
    pair_count = Counter(start[i:i+2] for i in range(len(start)-1))
    el_count = Counter(start)
    for _ in range(ITERATIONS):
        new_pair_count = Counter()

        for pair, n in pair_count.items():
            new_char = rules[pair]
            a,b = pair
            # for the amount of that pair, add the new pairs to the list 
            new_pair_count[a+new_char] += n
            new_pair_count[new_char+b] += n
            # New char is added to the count for each occurrence of the pair
            el_count[new_char] += n
            
        pair_count = new_pair_count

    return el_count


counts = solve(start,rules).most_common()
part1 = counts[0][1]-counts[-1][1]
counts = solve(start,rules, ITERATIONS=40).most_common()
part2 = counts[0][1]-counts[-1][1]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

