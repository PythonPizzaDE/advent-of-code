from dataclasses import dataclass, field
from typing import Protocol

@dataclass
class FileSystemMember(Protocol):
    name: str

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    parent: 'Self'
    files: list[FileSystemMember] = field(default_factory=list)

def resolve_dir(directory: str, current_directory: Directory) -> Directory:
    if directory == '..':
        return current_directory.parent
    for child in current_directory.files:
        if child.name == directory:
            return child
    new_directory = Directory(directory, current_directory)
    current_directory.files.append(new_directory)
    return new_directory

def resolve_file(file: str, size: int, current_directory: Directory) -> File:
    for child in current_directory.files:
        if child.name == file:
            return child
    new_file = File(file, size)
    current_directory.files.append(new_file)
    return new_file

def execute(inpt: str) -> Directory:
    command = ''
    root = Directory('/', None)
    current_directory = root
    for line in inpt.split('\n')[:-1]:
        if line == '$ ls':
            command = 'ls'
        elif line.startswith('$ cd'):
            command = 'cd'
            directory = line[5:]
            if directory == '/':
                current_directory = root
            else:
                current_directory = resolve_dir(directory, current_directory)
        elif line.startswith('dir '):
            resolve_dir(line[6:], current_directory)
        elif line[0].isnumeric():
            size, name = line.split(' ')
            resolve_file(name, int(size), current_directory)

    return root

def calculate_size(directory: Directory) -> int:
    size = 0
    for child in directory.files:
        if isinstance(child, Directory):
            size += calculate_size(child)
            continue
        size += child.size
    return size

def calculate_filtered_size(file_system: Directory, max_size: int = 100000) -> int:
    size = 0
    for child in file_system.files:
        if isinstance(child, Directory):
            calculated_size = calculate_size(child)
            if calculated_size <= max_size:
                size += calculated_size
            size += calculate_filtered_size(child, max_size)
    return size

def find_to_delete_size(file_system: Directory, needed: int, used: int, file_system_size: int, smallest: int = None) -> int:
    unused = file_system_size - used
    rest = needed - unused
    for child in file_system.files:
        if isinstance(child, Directory):
            size = calculate_size(child)
            if size >= rest and size <= (smallest or file_system_size):
                smallest = size
            smallest = find_to_delete_size(child, needed, used, file_system_size, smallest)
    return smallest

FILE_SYSTEM_SIZE   = 70000000
NEEDED_SPACE_TOTAL = 30000000

with open('input.txt') as file:
    inpt = file.read()

file_system = execute(inpt)
file_system_size = calculate_size(file_system)
# total size
print('total:\t', file_system_size)

print()

# maxed size
print('maxed:\t', calculate_filtered_size(file_system))

print()

# to delete size
print('delete:\t', find_to_delete_size(file_system, NEEDED_SPACE_TOTAL, file_system_size, FILE_SYSTEM_SIZE))
