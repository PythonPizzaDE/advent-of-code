def make_range(inpt: str) -> list[int]:
    lower, upper = map(int, inpt.split('-'))
    return list(range(lower, upper + 1))

def contains(range1: str, range2: str) -> bool:
    r1 = make_range(range1)
    r2 = make_range(range2)
    return r1[0] <= r2[0] and r1[-1] >= r2[-1]

def overlap(range1: str, range2: str) -> bool:
    r1 = make_range(range1)
    r2 = make_range(range2)
    for i in r1:
        for j in r2:
            if i == j:
                return True
    return False

def count_contains(inpt: str) -> int:
    count = 0
    for line in inpt.split('\n')[:-1]:
        r1, r2 = line.split(',')
        if contains(r1, r2) or contains(r2, r1):
            count += 1
    return count

def count_overlaps(inpt: str) -> int:
    count = 0
    for line in inpt.split('\n')[:-1]:
        r1, r2 = line.split(',')
        if overlap(r1, r2):
            count += 1
    return count

with open('input.txt') as file:
    inpt = file.read()

# part 1
print(count_contains(inpt))

print('='*40)

# part 2
print(count_overlaps(inpt))
