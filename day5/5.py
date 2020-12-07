from timeit import default_timer as timer

def get_input():
    with open("./day5/5.in","r") as f:
        return [line.strip()for line in f.readlines()]


p1start = timer()
res = []
decoding = {'F':'0', 'B':'1', 'L':'0', 'R':'1'}
for barcode in get_input():
    row, col = barcode[:7], barcode[7:]
    row_bin, col_bin = '0b', '0b'
    for letter in row:
        row_bin += decoding[letter]
    for letter in col:
        col_bin += decoding[letter]
    row, col = int(row_bin, 2), int(col_bin, 2)
    res.append((row*8) + col)
p1 = max(res)
p1end = timer()

p2start = timer()
res.sort()
for i in range(len(res)):
    if res[i+1] - res[i] == 2:
        p2 = res[i] + 1
        break
p2end = timer()


print("Day 5: Binary Boarding")
print(f"Part 1: {p1} in {p1end-p1start}s.")
print(f"Part 2: {p2} in {p2end-p2start}s.")