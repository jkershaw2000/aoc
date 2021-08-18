def get_input():
    with open("./day2/2.in", "r") as f:
        return [int(val) for val in f.read().split(",")]

program = get_input()

def intcode_computer(program, *inputs):
    for idx, val in enumerate(inputs):
        program[idx+1] = val

    pc = 0
    while True:
        if program[pc] == 99:
            # HALTING
            break
        elif program[pc] == 1:
            # ADD a b c, c = a + b
            program[program[pc+3]] = program[program[pc+1]] + program[program[pc+2]]
            pc += 4
        elif program[pc] == 2:
            program[program[pc+3]] = program[program[pc+1]] * program[program[pc+2]]
            pc += 4
    return program[0]

p1 =  intcode_computer(program, 12, 2) 
print(p1)

for a in range(100):
    for b in range(100):
        if intcode_computer(program, a, b) == 19690720:
            print(100 * a + b)
            break
