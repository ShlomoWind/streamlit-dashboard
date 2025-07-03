#תרגיל מספר 1
def convert_temp(value,to_scale):
    try:
        temp = float(value)
    except:
        return "Invalid input, please enter a number"
    if to_scale == 'F':
        return(temp * 9/5) + 32
    elif to_scale == 'C':
        return(temp - 32) * 5/9
    else:
        return "Invalid unit"

#תרגיל מספר 2
def sum_and_max(*sum_numbers):
    even = [x for x in sum_numbers if x % 2 == 0]
    odd = [x for x in sum_numbers if x % 2]

    sum_even = sum(even)
    if not odd:
        return sum_even * 0
    else:
        max_odd = max(odd)
        return sum_even * max_odd

#תרגיל מספר 3
def to_upper(string_list):
    return list(map(lambda x:x.upper() +"!",string_list))
print(to_upper(["hello", "world", "python"]))

#תרגיל מספר 4
target_bank = []

def add_target(coords,name,confidence):
    global target_bank
    if not isinstance(coords, tuple) or len(coords) != 2:
        return "Invalid coordinates"
    if not isinstance(name, str) or not name.strip():
        return "Invalid name"
    if not isinstance(confidence, int) or not (1 <= confidence <= 10):
        return "Invalid confidence (1–10)"
    target_dict = {"coords":coords,"name":name,"confidence":confidence}
    target_bank.append(target_dict)

def delete_target(name_or_coords):
    global target_bank
    target_bank = [t for t in target_bank if t["coords"] != name_or_coords and t["name"] != name_or_coords]

def display_targets(confidence = 0):
    global target_bank
    if not target_bank:
        return "no targets"
    else:
        for t in target_bank:
            if t["confidence"] >= confidence:
                print(f"Name: {t['name']}, Coords: {t['coords']}, Confidence: {t['confidence']}")