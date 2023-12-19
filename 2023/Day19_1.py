from os import path

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

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
#  input = f.read()


def process_part(part):
    global rules
    rule_key = "in"
    while True:
        for rule in rules[rule_key]:
            if len(rule) == 1:
                rule_key = rule[0]
            else:
                field_key, condition, amount, destination = rule
                if condition == "<":
                    if part[field_key] < amount:
                        rule_key = destination
                        break
                elif condition == ">":
                    if part[field_key] > amount:
                        rule_key = destination
                        break
        if rule_key in ("R", "A"):
            break

    return rule_key


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

    sums = 0
    for part in parts:
        accepted = process_part(part)
        if accepted == "A":
            sums += sum(part.values())

    print(sums)
