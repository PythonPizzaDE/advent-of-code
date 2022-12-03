from string import ascii_letters

priorities = {c : i + 1 for i, c in enumerate(ascii_letters)}

def parse_rucksacks(inpt: str) -> list[tuple[str]]:
    rucksacks = []
    for line in inpt.split('\n'):
        if line == '':
            continue
        first = line[:(len(line)//2)]
        second = line[(len(line)//2):]
        rucksacks.append((first, second))
    return rucksacks


def item_letter(rucksack: tuple[str]) -> str:
    first = {}
    second = {}
    for char in rucksack[0]:
        first[char] = True

    for char in rucksack[1]:
        second[char] = True

    for char in first.keys():
        if second.get(char, False):
            return char

def badge_letter(rucksacks: tuple[str]) -> str:
    first = {}
    second = {}
    third = {}
    for char in rucksacks[0]:
        first[char] = True

    for char in rucksacks[1]:
        second[char] = True

    for char in rucksacks[2]:
        third[char] = True

    for char in first.keys():
        if second.get(char, False) and third.get(char, False):
            return char

def item_priority_sum(inpt: str) -> int:
    rucksacks = parse_rucksacks(inpt)
    priority_sum = 0
    for rucksack in rucksacks:
        priority_sum += priorities[item_letter(rucksack)]
    return priority_sum

def badge_priority_sum(inpt: str) -> int:
    lines = inpt.split('\n')[:-1]
    priority_sum = 0
    while lines != []:
        first = lines.pop()
        second = lines.pop()
        third = lines.pop()
        rucksacks = (first, second, third)
        letter = badge_letter(rucksacks)
        priority_sum += priorities[letter]
    return priority_sum


with open('input.txt') as file:
    inpt = file.read()


print(item_priority_sum(inpt))
print(badge_priority_sum(inpt))

