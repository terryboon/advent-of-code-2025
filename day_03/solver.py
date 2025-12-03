day_str = "03"

def parse_input(filename):
    # Convert input file to a list of lists (each bank corresponds to a list)
    data_in = []

    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            data_in.append([int(digit) for digit in line])
    
    return(data_in)

def solver_1(data_in):
    joltages = [max_bank_joltage(bank_list) for bank_list in data_in]
    return(sum(joltages))

def solver_2(data_in):
    joltages = [max_bank_joltage_2(bank_list, 12) for bank_list in data_in]
    return(sum(joltages))

def max_bank_joltage(bank_list):
    max_digit_1 = max(bank_list[:-1])
    max_digit_1_pos = bank_list.index(max_digit_1)
    max_digit_2 = max(bank_list[max_digit_1_pos+1:])
    return((10 * max_digit_1) + max_digit_2)

def max_bank_joltage_2(bank_list, num_batteries):
    on_batteries = []
    start = 0

    for battery_idx in range(num_batteries):
        max_digit = max(bank_list[start:(len(bank_list)-(num_batteries-battery_idx-1))])
        max_digit_pos = bank_list.index(max_digit, start)
        on_batteries.append(max_digit)
        start = max_digit_pos + 1

    joltage = sum([battery * (10 ** (num_batteries - battery_idx - 1))
                   for (battery_idx, battery) in enumerate(on_batteries)])
    return(joltage)



def process_part_1(filename):
    data_in = parse_input(filename)
    result = solver_1(data_in)
    return(result)

def process_part_2(filename):
    data_in = parse_input(filename)
    result = solver_2(data_in)
    return(result)