import json
from copy import deepcopy

def generate_conditions(tag, start, origin, pos_min, pos_max):
    condition = {
        "condition": "location_check",
        "offsetX": 0,
        "offsetY": 0,
        "offsetZ": 0,
        "predicate": {
            "position": {
                "x": 0.5,
                "y": 0.5,
                "z": 0.5
            },
            "block": {
                "tag": tag
            }
        }
    }

    conditions = []

    pos = [b - a for a,b in zip(start, origin)]

    for x in range(pos_min[0], pos_max[0] + 1):
        for y in range(pos_min[1], pos_max[1] + 1):
            for z in range(pos_min[2], pos_max[2] + 1):
                new_condition = deepcopy(condition)
                new_condition["offsetX"] += pos[0] + x
                new_condition["offsetY"] += pos[1] + y
                new_condition["offsetZ"] += pos[2] + z
                new_condition["predicate"]["position"]["x"] += origin[0] + x
                new_condition["predicate"]["position"]["y"] += origin[1] + y
                new_condition["predicate"]["position"]["z"] += origin[2] + z
                conditions.append(new_condition)
            
    with open(tag + ".json", "w") as f:
        f.write(json.dumps(conditions, separators=(',', ':')))

start = (0, 8, 2)
origin = (0, 0, 0)
pos_min = (0, 0, 0)
pos_max = (7, 7, 0)
generate_conditions("a", start, origin, pos_min, pos_max)
generate_conditions("b", start, origin, pos_min, pos_max)
