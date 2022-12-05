def top(inpt: str) -> str:
    return inpt.split('\n\n')[0]

def bottom(inpt: str) -> str:
    return inpt.split('\n\n')[1]
def parse_top(inpt: str) -> list[list[str]]:
    result = [[] for _ in range(9)]
    for line in inpt.split('\n')[:-1]:
        for column, content in enumerate(line):
            if content in '[] ':
                continue
            stack_index = int(((column + 1) / 4) - 0.5)
            result[stack_index].insert(0, content)
    return result

def parse_instruction(instruction: str) -> tuple[int]:
    nums = []
    num_string = ''
    for char in instruction:
        if char.isnumeric():
            num_string += char
        elif num_string != '':
            nums.append(int(num_string))
            num_string = ''
    if num_string != '':
        nums.append(int(num_string))
    return tuple(nums)

def execute(inpt: str) -> str:
    stacks = parse_top(top(inpt))
    for line in bottom(inpt).split('\n')[:-1]:
        instruction = parse_instruction(line)
        for _ in range(instruction[0]):
            item = stacks[instruction[1] - 1].pop()
            stacks[instruction[2] - 1].append(item)

    result = ''
    for stack in stacks:
        result += stack[-1]
    return result

def execute_new(inpt: str) -> str:
    stacks = parse_top(top(inpt))
    for line in bottom(inpt).split('\n')[:-1]:
        instruction = parse_instruction(line)
        count = instruction[0]
        items = stacks[instruction[1] - 1][-count:]
        stacks[instruction[1] - 1] = stacks[instruction[1] - 1][:-count]
        stacks[instruction[2] - 1].extend(items)

    result = ''
    for stack in stacks:
        result += stack[-1]
    return result


with open('input.txt') as file:
    inpt = file.read()

# part 1
print(execute(inpt))

print('='*40)

# part 2
print(execute_new(inpt))
