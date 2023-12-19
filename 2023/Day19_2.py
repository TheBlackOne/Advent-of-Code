from os import path
from Utils import *

input = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

rules = {}
parts = []
accepted_counters = []

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
# input = f.read()


def process_part_rec(rule_key, part):
    global rules
    if rule_key == "A":
        accepted_counters.append(part)
        return
    if rule_key == "R":
        return
    else:
        for rule in rules[rule_key]:
            if len(rule) == 1:
                new_rule_key = rule[0]
                process_part_rec(new_rule_key, part)
            else:
                field_key, condition, amount, destination = rule
                current_field = part[field_key]

                lower_field = set(range(1, amount + 1))
                higher_field = set(range(amount, 4001))

                if condition == "<":
                    new_field = current_field - higher_field
                elif condition == ">":
                    new_field = current_field - lower_field

                part[field_key] = current_field - new_field

                new_part = part.copy()
                new_part[field_key] = new_field

                process_part_rec(destination, new_part)


if __name__ == "__main__":
    rule_string, parts_string = input.split("\n\n")
    for line in rule_string.splitlines():
        key, rule_string = line[:-1].split("{")
        rules_list = []
        for rule in rule_string.split(","):
            if ":" not in rule:
                rules_list.append(list([rule]))
            else:
                rule, destination = rule.split(":")
                field = rule[0]
                condition = rule[1:2]
                amount = rule[2:]
                rules_list.append((field, condition, int(amount), destination))
        rules[key] = rules_list

    for line in parts_string.splitlines():
        part = {}
        fields = line[1:-1].split(",")
        for field in fields:
            field_key, amount = field.split("=")
            part[field_key] = int(amount)
        parts.append(part)

    part = {
        "x": set(range(1, 4001)),
        "m": set(range(1, 4001)),
        "a": set(range(1, 4001)),
        "s": set(range(1, 4001)),
    }

    result = 0
    process_part_rec("in", part)
    for part in accepted_counters:
        result += prod([len(f) for f in part.values()])
    print(result)
