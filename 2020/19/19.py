import re

rules, messages = [section.replace('"','').split('\n') for section in open('input2.in').read().split('\n\n')]

validation = {}
for rule in rules:
    num, matches = rule.split(': ')
    if '|' in matches:
        matches = [match.split() for match in matches.split(' | ')]
    # elif len(matches) > 1:
    else:
        matches = matches.split()
    #     pass
    validation[num] = matches

# print(validation)

def get_regex(rule):
    value = validation[rule]
    if isinstance(value, str):
        pass
    # 'base case'
    elif value[0] == 'a' or value[0]=='b':
        validation[rule] = value[0]

    # the trivial case
    elif len(value) == 1:
        validation[rule] = get_regex(value[0])
    
    # 'or' case
    elif len(value) >1 and isinstance(value[0], list):
        validation[rule] = '(' + ''.join([get_regex(r) for r in value[0]]) + '|' + ''.join([get_regex(r) for r in value[1]]) + ')'
    
    # 'and' case
    else:
        validation[rule] = ''.join([get_regex(r) for r in value])
    return validation[rule]

rule_42 = get_regex('42')
rule_31 = get_regex('31')

# zero_rule = '^'+get_regex('0')+'$'
rule_11 = '('
for i in range(1,10):
    rule_11+='('+rule_42+'{'+str(i)+'}'+rule_31+'{'+str(i)+'})' +'|'
zero_rule = '^'+ rule_42 + '+' + rule_11[:-1] + ')$'

num_matches = 0
pattern = re.compile(zero_rule)
for message in messages:
    num_matches += int(bool(pattern.match(message)))
print(num_matches)

