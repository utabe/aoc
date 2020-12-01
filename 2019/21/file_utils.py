import os


def read_intcode(file) -> list:
    with open(file) as f:
        return list(map(int, f.read().split(',')))


def read_map(file) -> list:
    with open(file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]


def read_lines(file) -> list:
    with open(file) as f:
        return [line.rstrip() for line in f.readlines()]


def read_integers(file: str) -> list:
    with open(file) as f:
        return list(map(int, [x for x in f.read()]))


def get_path(dir_name: str, filename: str) -> str:
    return os.path.join(os.path.dirname(dir_name), filename)
