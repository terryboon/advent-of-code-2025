day_str = "01"

def parse_input(filename):
    # Convert input file to a list of 2-tuples like ("L", 68)
    data_in = []

    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            data_in.append((line[0], int(line[1:])))
    
    return(data_in)

def solver_1(data_in):
    num_zeros = calc_zeros(data_in)
    return(num_zeros)

def solver_2(data_in):
    num_zeros = calc_zeros_2(data_in)
    return(num_zeros)

def calc_zeros(data_in):
    pos = 50
    num_zeros = 0

    for (direction, num_clicks) in data_in:
        if direction == "R":
            pos = (pos + num_clicks) % 100
        elif direction == "L":
            pos = (pos - num_clicks) % 100
        else:
            raise(ValueError)

        if pos == 0:
            num_zeros += 1
    
    return(num_zeros)

def calc_zeros_2(data_in):
    pos = 50
    num_zeros = 0

    for (direction, num_clicks) in data_in:
        if direction == "R":
            num_zeros += (pos + num_clicks) // 100
            pos = (pos + num_clicks) % 100
        elif direction == "L":
            # Reflect coordinates
            # Starting from (100-pos) and going num_clicks R gets same number of zeros as
            # starting at pos and going num_clicks L.
            num_zeros += (((-pos) % 100) + num_clicks) // 100
            pos = (pos - num_clicks) % 100
        else:
            raise(ValueError)

    return(num_zeros)




def process_part_1(filename):
    data_in = parse_input(filename)
    result = solver_1(data_in)
    return(result)

def process_part_2(filename):
    data_in = parse_input(filename)
    result = solver_2(data_in)
    return(result)