def intcode_computer(program, *inputs):
    for idx, val in enumerate(inputs):
        program[idx+1] = val

    pc = 0
    while True:

        opcode = program[pc] % 10 

        # Get parameter modes of each paramter
        try:
            param1 = program[pc+1] if (program[pc] // 100) % 10 == 1 else program[program[pc+1]] 
        except IndexError:
            param1 = None
        try:
            param2 = program[pc+2] if (program[pc] // 1000) % 10 == 1 else program[program[pc+2]] 
        except IndexError:
            param2 = None
        try:
            param3 = program[pc+3] if (program[pc] // 10000) % 10 == 1 else program[program[pc+3]] 
        except IndexError:
            param3 = None
            
        if program[pc] == 99:
            # HALT
            break
        elif opcode == 1:
            # ADD
            program[program[pc+3]] = param1 + param2
            pc += 4
        elif opcode == 2:
            # MULTIPLY
            program[program[pc+3]] = param1 * param2
            pc += 4
        elif opcode == 3:
            # INPUT
            program[program[pc+1]] = int(input("Input: "))
            pc += 2
        elif opcode == 4:
            # OUTPTU
            print("Output: ", program[program[pc+1]])
            pc += 2
        elif opcode == 5:
            # JUMP IF TRUE
            pc = param2 if param1 != 0 else pc + 3
        elif opcode == 6:
            # JUMP IF FALSE
            pc = param2 if param1 == 0 else pc + 3
        elif opcode == 7:
            # LESS THAN
            program[program[pc+3]] = 1 if param1 < param2 else 0
            pc += 4
        elif opcode == 8:
            # EQUAL TO
            program[program[pc+3]] = 1 if param1 == param2 else 0
            pc += 4
        else:
            print("this is a problem")
