# visited_indexes = set()
with open('input.in') as file:
    instructions = file.read().split('\n')


target_index = len(instructions)


def read_index(index, accumulator, instruct=instructions):
    instruction, value = instruct[index].split()
    value = int(value)
    if instruction == 'acc':
        accumulator += value
        index += 1
    elif instruction == 'nop':
        index +=1
    elif instruction == 'jmp':
        index += value
    else:
        raise IndexError
    return index, accumulator

def run_instructions(instruct=instructions, visited_indexes = set(), accumulator = 0):
    index = 0
    while index not in visited_indexes and index != target_index:
        visited_indexes.add(index)
        index, accumulator = read_index(index,accumulator, instruct)
    return index, accumulator
index,accumulator = run_instructions()
print(f'Repeated index was {index} with accumulator value {accumulator}')

for i in range(len(instructions)):
    if instructions[i].startswith('jmp'):
        modified_instructions = instructions[:]
        modified_instructions[i] = modified_instructions[i].replace('jmp','nop')
        index, accumulator = run_instructions(instruct=modified_instructions,visited_indexes=set())
    elif instructions[i].startswith('nop'):
        modified_instructions = instructions[:]
        modified_instructions[i] = modified_instructions[i].replace('nop','jmp')
        index, accumulator = run_instructions(instruct=modified_instructions, visited_indexes=set())
    if index == target_index:
        print(f"Instruction to change was {instructions[i]} at index {i} with accumulator value {accumulator}")
        break
