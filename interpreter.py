# test_input: str = "++++++++++[->++++++++<]>+++.<+++++[->++++<]>++.++++.++.-.---------.--<++++++[->>++++++<<]>>----.<.<+++++[->>+++++<<]>>+." # Simone c:

while True:
    input_value = input("Insert the brainfuck code: ")

    memory_cell: list = list(0 for i in range(5))
    head_position = 0
    loop_start_pos = 0
    loop_end_pos = 0
    index = 0

    if(input_value.lower() == "exit"): 
        break

    while True:
        if(index >= len(input_value)): break

        match input_value[index]:
            case "+":
                try:
                    memory_cell[head_position] += 1
                except IndexError:
                    memory_cell += 0
                    memory_cell[head_position] += 1
            case "-":
                try:
                    memory_cell[head_position] -= 1
                except IndexError:
                    memory_cell += 0
                    memory_cell[head_position] -= 1
            case ">":
                head_position += 1
                # print(f"New head position: {head_position}")
            case "<":
                head_position -= 1
                # print(f"New head position: {head_position}")
            case ".":
                print(chr(memory_cell[head_position]), end='')
            case "[":
                loop_start_pos = index
            case "]":
                if memory_cell[head_position] != 0:
                    loop_end_pos = index
                    index = loop_start_pos
                else:
                    index = loop_end_pos
            case _:
                print("Unknown value, continuing...")
            
        index += 1
        # print(f"Current memory cell value: {memory_cell[head_position]}")