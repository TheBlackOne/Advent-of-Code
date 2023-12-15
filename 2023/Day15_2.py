input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

# with open("input.txt") as f:
#    input = f.read()

boxes = []


def hash(input):
    current = 0
    for c in input:
        current += ord(c)
        current *= 17
        current = current % 256
    return current


if __name__ == "__main__":
    for i in range(256):
        boxes.append({})

    for step in input.split(","):
        if "=" in step:
            label, focal = step.split("=")
            box_id = hash(label)

            boxes[box_id][label] = focal
        elif "-" in step:
            label, _ = step.split("-")
            box_id = hash(label)
            if label in boxes[box_id].keys():
                del boxes[box_id][label]

    result = 0
    for box_id, box in enumerate(boxes):
        for slot_id, (_, focal) in enumerate(box.items()):
            result += (box_id + 1) * (slot_id + 1) * int(focal)

    print(result)
