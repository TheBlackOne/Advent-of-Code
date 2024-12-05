input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# with open("input.txt") as f:
#    input = f.read()

rules = None
updates = None


def get_relevant_rules(page):
    result = []
    for rule in rules:
        if page in rule:
            result.append(rule)
    return rules


def check_update(pages):
    breaking_rule = None

    for page in pages:
        page_index = update.index(page)
        for rule in get_relevant_rules(page):
            first, second = rule.split("|")
            if page == first:
                if second in update:
                    second_index = update.index(second)
                    if second_index < page_index:
                        # right_order = False
                        breaking_rule = (first, second)
                        # print(rule)
                        break
            elif page == second:
                if first in update:
                    first_index = update.index(first)
                    if first_index > page_index:
                        # right_order = False
                        breaking_rule = (first, second)
                        # print(rule)
                        break
    return breaking_rule


def fix_update(pages, breaking_rule):
    first, second = breaking_rule
    first_index = pages.index(first)
    second_index = pages.index(second)

    pages[first_index], pages[second_index] = (
        pages[second_index],
        pages[first_index],
    )
    return pages


if __name__ == "__main__":
    sum = 0
    rules, updates = input.split("\n\n")
    rules = rules.splitlines()

    for update in updates.splitlines():
        pages = update.split(",")
        check_counter = 0

        while True:
            check_counter += 1
            breaking_rule = check_update(pages)
            if breaking_rule is not None:
                update = fix_update(pages, breaking_rule)
            else:
                break

        if check_counter > 1:
            # print(update)
            middle = pages[len(pages) // 2]
            sum += int(middle)

    print(sum)
