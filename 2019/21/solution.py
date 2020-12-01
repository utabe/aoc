from file_utils import read_intcode
from intcode import Intcode


def run_springscript(vm: Intcode) -> (int, str):
    ascii_image = []
    while True:
        ascii_int = vm.run_until_io_or_done()
        if ascii_int is None:
            break
        if ascii_int > 127:  # ascii table size
            return ascii_int, ''
        ascii_image.append(chr(ascii_int))
    return -1, ''.join(ascii_image)


def load_springscript(vm: Intcode, script: list):
    ascii_chars = list(map(ord, list('\n'.join(script) + '\n')))
    while len(ascii_chars) > 0:
        ascii_int = ascii_chars.pop(0)
        vm.set_input(ascii_int)
        vm.run_until_input_or_done()


def get_hull_damage(vm: Intcode, script: list) -> int:
    load_springscript(vm, script)
    damage, ascii_images = run_springscript(vm)
    if ascii_images:
        print(ascii_images)
    return damage


def part_one(filename: str) -> int:
    # (!A or !B or !C) and D
    script = [
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'WALK']
    return get_hull_damage(Intcode(read_intcode(filename)), script)


def part_two(filename: str) -> int:
    script = [
        # (!A or !B or !C) and D and (E or H)
        # Inferred experimentally by inspecting the failed scenarios
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'NOT E T',
        'NOT T T',
        'OR H T',
        'AND T J',
        'RUN']
    return get_hull_damage(Intcode(read_intcode(filename)), script)

print(part_one('input.in'))
print(part_two('input.in'))
