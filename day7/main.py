from dataclasses import dataclass, field
from typing import Protocol

@dataclass
class FileSystemMember(Protocol):
    name: str
    size: int

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
            current_directory = resolve_dir(line[5:], current_directory)
        elif line.startswith('$ dir '):
            resolve_dir(line[6:], current_directory)
        elif line[0].isnumeric():
            size, name = line.split(' ')
            resolve_file(name, int(size), current_directory)

    return root

with open('input.example.txt') as file:
    inpt = file.read()

print(execute(inpt))
