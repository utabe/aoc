import itertools
from collections import defaultdict
rules, my_ticket, nearby_tickets = [section.split('\n') for section in open('input.in').read().split('\n\n')]

my_ticket = [int(i) for i in my_ticket[1].split(',')]
nearby_tickets = [list(map(int,ticket.split(','))) for ticket in nearby_tickets[1:]]

valid_nums = set()
rules_dict = defaultdict(set)
for rule in rules:
    rule_name = rule.split(':')[0]
    ranges = rule.split(': ')[1].split(' or ')
    for range_ in ranges:
        mn, mx = map(int,range_.split('-'))
        valid_nums.update(range(mn,mx+1))
        rules_dict[rule_name].update(range(mn,mx+1))

possible_rule_positions = {pos:set(range(len(my_ticket))) for pos in rules_dict.keys()}
for ticket in nearby_tickets:
    if any(num not in valid_nums for num in ticket):
        continue
    else:
        for i, num in enumerate(ticket):
            for rule_name,possibilities in possible_rule_positions.items():
                if num not in rules_dict[rule_name]:
                    possible_rule_positions[rule_name].discard(i)

for _ in range(len(my_ticket)):
    for k,v in possible_rule_positions.items():
        if len(v) == 1:
            for key, val in possible_rule_positions.items():
                if v != val:
                    possible_rule_positions[key] -= v

# Part 1
invalid_nums = 0
for ticket_num in itertools.chain.from_iterable(nearby_tickets):
    if ticket_num not in valid_nums:
        invalid_nums += ticket_num
print(invalid_nums)

# Part 2
departure_value = 1
for rule_name, val in possible_rule_positions.items():
    if rule_name.startswith('departure'):
        departure_value *= my_ticket[next(iter(val))]
print(departure_value)
