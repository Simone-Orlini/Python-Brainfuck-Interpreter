test_input: str = "++++++++++[->++++++++<]>+++.<+++++[->++++<]>++.++++.++.-.---------.--<++++++[->>++++++<<]>>----.<.<+++++[->>+++++<<]>>+." # Simone c:

memory_cell: list = list(0 for i in range(5))
head_position = 0
loop_start_pos = 0
loop_end_pos = 0
index = 0

while True:
    if(index >= len(test_input)): break

    match test_input[index]:
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
        
    index += 1
    # print(f"Current memory cell value: {memory_cell[head_position]}")