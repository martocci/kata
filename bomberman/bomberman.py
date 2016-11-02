 # https://www.hackerrank.com/challenges/bomber-man

import sys

def write_output(dict_final, row_total, column_total):
    '''
    Output . where there is an entry in the key
    '''

    final_state = [["O"]*(column_total) for n in range(row_total)]

    for key in dict_final:
        final_state[key[0]][key[1]] = "."

    for row in final_state:
        row_string = ''.join(row)
        # print results:
        print(row_string)

    exit()

def insert_position(state_dict, row_count, cell_count, row_total, column_total):
    '''
    Insert a bomb position + its neighbors
    '''

    state_dict[(row_count, cell_count)] = None
    if row_count > 0:
        state_dict[(row_count - 1, cell_count)] = None
    if row_count < row_total - 1:
        state_dict[(row_count + 1, cell_count)] = None
    if cell_count > 0:
        state_dict[(row_count, cell_count - 1)] = None
    if cell_count < column_total - 1:
        state_dict[(row_count, cell_count + 1)] = None

    return state_dict

# row_0 = "6 7 13"
# row_initial = [
#             ".......",
#             "...0...",
#             "....0..",
#             ".......",
#             "00.....",
#             "00....."]

# row_0 = "3 3 13"
# row_initial = ["0.0", ".0.", "..."]

row_total, column_total, time_final = None, None, None
row_initial = []

# read in info:
for line in sys.stdin:
    if row_total is None:
        row_total, column_total, time_final = line.split(" ")
        row_total = int(row_total)
        column_total = int(column_total)
        time_final = int(time_final)
    else:
        row_initial.append(line.strip('\n'))

if time_final == 0 or time_final == 1:
    # if t <= 1, then the state is still in the initial state:
    for row in row_initial:
        # print results
        print(row)
    exit()

elif time_final%2 == 0 and time_final > 0:
    # If t is even, the grid is always filled with bombs:
    # print results
    row_full = "O" * column_total
    for i in range(0, row_total):
        print(row_full)
    exit()

# Create initial dict
state_dict = {}
row_count = 0
for row in row_initial:
    cell_count = 0
    for cell in row:
        if cell == "O":
            # This is a bomb's position
            state_dict = insert_position(state_dict, row_count, cell_count, row_total, column_total)
        cell_count = cell_count + 1
    row_count = row_count + 1

#Keep a record of past timestep states, so the code will stop when a stable cycle is reached
state_dict_1 = state_dict.copy()

for time in range(int((time_final-1)/2)):

    # advance to the next timestep, new prior states
    state_dict_2 = state_dict_1.copy()
    state_dict_1 = state_dict.copy()
    state_dict = {}

    for row_count in range(row_total):
        for cell_count in range(column_total):
            if (row_count, cell_count) not in state_dict_1:
                state_dict = insert_position(state_dict, row_count, cell_count, row_total, column_total)
            cell_count = cell_count + 1
        row_count = row_count + 1

    if state_dict == state_dict_2 and int((time_final-2*time+3)%4) == 0:
        # reached a "stable" solution
        write_output(state_dict, row_total, column_total)

write_output(state_dict_1, row_total, column_total)


