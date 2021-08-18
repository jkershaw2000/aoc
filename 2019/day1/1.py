def get_input():
    with open("./day1/1.in", "r") as f:
        return [int(val) for val in f.read().split("\n")]

def calculate_fuel(m):
    return (m // 3) -2

def calculate_fuels_fuel(m):
    ans = 0
    while m > 0:
        m = max((m // 3) -2, 0)
        ans += m
    return ans


p1 =  sum([calculate_fuel(val) for val in get_input()])
print(p1)

p2 = sum([calculate_fuels_fuel(calculate_fuel(val)) + calculate_fuel(val)  for val in get_input()])
print(p2)

    
   