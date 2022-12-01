with open('input.txt') as file:
    inpt = file.read()

def parse_calories(string: str) -> list[str]:
    calories = []
    sub_string = ''
    for line in string.split('\n'):
        if line == '' and sub_string != '':
            calories.append(sub_string)
            sub_string = ''
            continue
        sub_string += f'{line}\n'

    return calories

def get_max_calories(calories_list: list[str]) -> int:
    max_value = 0
    for calories_str in calories_list:
        calories = 0
        calories_int_list = []
        for line in calories_str.split('\n'):
            if line != '':
                calories += int(line)
        if calories > max_value:
            max_value = calories

    return max_value

print(get_max_calories(parse_calories(inpt)))

def get_top_calories(calories_list: list[str]) -> list[int]:
    elve_calories = []
    for calories_str in calories_list:
        calories = 0
        calories_int_list = []
        for line in calories_str.split('\n'):
            if line != '':
                calories += int(line)
        elve_calories.append(calories)

    return list(reversed(sorted(elve_calories)))[:3]

print(sum(get_top_calories(parse_calories(inpt))))
