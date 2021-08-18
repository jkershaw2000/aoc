import computer

def get_input():
    with open("./day5/5.in", "r") as f:
        return [int(val) for val in f.read().split(",")]

program = get_input()
computer.intcode_computer(program)