 # https://www.hackerrank.com/challenges/bomber-man

def write_output(dict_final, row_total, column_total):
    '''
    Output . where there is an entry in the key
    '''

    final_state = [["0"]*(column_total) for n in range(row_total)]

    for key in dict_final:
        #print("key = ", key)
        final_state[key[0]][key[1]] = "."

    for row in final_state:
        row_string = ''.join(row)
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



# row_0 = "6 7 11"
#
# row_initial = [
#             ".......",
#             "...0...",
#             "....0..",
#             ".......",
#             "00.....",
#             "00....."]

row_0 = "3 3 13"
row_initial = ["0.0", ".0.", "..."]

row_0 = row_0.split(" ")

# read in info:
row_total = int(row_0[0])
column_total = int(row_0[1])
time_final = int(row_0[2])

if time_final == 0 or time_final == 1:
    # if t <= 1, then the state is still in the initial state:
    for row in row_initial:
        print(row)
    exit()

elif time_final%2 == 0 and time_final > 0:
    # If t is even, the grid is always filled with bombs:
    row_full = "0" * column_total
    for i in range(0, row_total):
        print(row_full)
    exit()

# Create initial dict
state_dict = {}
row_count = 0
for row in row_initial:
    cell_count = 0
    for cell in row:
        if cell == "0":
            # This is a bomb's position
            state_dict = insert_position(state_dict, row_count, cell_count, row_total, column_total)
        cell_count = cell_count + 1
    row_count = row_count + 1

#Keep a record of past timestep states, so the code will stop when a stable cycle is reached
state_dict_1 = {}

for time in range(int((time_final-1)/2)):

    print("time = ", (time*2 + 3), time, time_final)

    state_dict_2 = state_dict_1.copy()
    state_dict_1 = state_dict.copy()
    state_dict = {}

    for row_count in range(row_total):
        for cell_count in range(column_total):
            if (row_count, cell_count) not in state_dict_1:
                state_dict = insert_position(state_dict, row_count, cell_count, row_total, column_total)
            cell_count = cell_count + 1
        row_count = row_count + 1

    print("state = ", state_dict)
    print("state1 = ", state_dict_1)
    print("state2 = ", state_dict_2)

    if state_dict == state_dict_2 and int((time_final-2*time+3)%4) == 0:
        # reached a "stable" solution
        print("exit with stable soln at t = ", (time*2 + 5), time)
        write_output(state_dict, row_total, column_total)

write_output(state_dict_1, row_total, column_total)








