def check_doubles(l: list) -> bool:
    for i in range(len(l)):
        if l[i] in l[:i]:
            return True
    return False


def find_marker(inpt: str, marker_length) -> int:
    for i in range(len(inpt) - marker_length + 1):
        window = inpt[i: i + marker_length]
        if not check_doubles(window):
            return i + marker_length

with open('input.txt') as file:
    inpt = file.read()

# packet markers
print(find_marker(inpt, 4))

print('='*40)

# message markers
print(find_marker(inpt, 14))
