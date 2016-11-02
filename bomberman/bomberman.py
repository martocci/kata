 # https://www.hackerrank.com/challenges/bomber-man

def write_output(dict_final, row_total, column_total):
    '''
    Output . where there is an entry in the key
    '''

    #print("dict_final = ", dict_final)

    final_state = [["0"]*(column_total) for n in range(row_total)]

    for key in dict_final:
        #print("key = ", key)
        final_state[key[0]][key[1]] = "."
        #print(final_state)

    #print('final state = ', final_state)

    for row in final_state:
        row_string = ''.join(row)
        print(row_string)
    exit()

def time_pass():
    '''
    Advance time step by 2 seconds
    '''
    pass



# Input:
# R C N
# grid of initial bombs
#
# R = # of rows
# C = # of columns
# N = # of seconds
#
# Input example:
# 6 7 3
# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....

row_0 = "6 7 3"

row_initial = [
            ".......",
            "...0...",
            "....0..",
            ".......",
            "00.....",
            "00....."]

# row_0 = "3 3 9"
# row_initial = ["0.0", ".0.", "..."]

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
            state_dict[(row_count, cell_count)] = None
            # Add all of the neighboring cells:
            if row_count > 0:
                state_dict[(row_count-1, cell_count)] = None
            if row_count < row_total-1:
                state_dict[(row_count+1, cell_count)] = None
            if cell_count > 0:
                state_dict[(row_count, cell_count - 1)] = None
            if cell_count < column_total-1:
                state_dict[(row_count, cell_count + 1)] = None
        cell_count = cell_count + 1
    row_count = row_count + 1

state_dict_1 = state_dict.copy()
state_dict_2 = {}
state_dict = {}

for time in range(time_final+1):
    #print("time = ", int(time*2 + 1), time_final)
    if int(time*2 + 1) == time_final+2:
        # reached the final time
        write_output(state_dict_1, row_total, column_total)

    for row_count in range(row_total):
        for cell_count in range(column_total):
            if (row_count,cell_count) not in state_dict_1:
                state_dict[(row_count,cell_count)] = None
                if row_count > 0:
                    state_dict[(row_count - 1, cell_count)] = None
                if row_count < row_total-1 :
                    state_dict[(row_count + 1, cell_count)] = None
                if cell_count > 0:
                    state_dict[(row_count, cell_count - 1)] = None
                if cell_count  < column_total-1:
                    state_dict[(row_count, cell_count + 1)] = None
            cell_count = cell_count + 1
        row_count = row_count + 1
    #print("time = ", int(time*2 + 1))
    #print("state_dict = ", state_dict)
    #print("new state = ", state_dict)
    if state_dict == state_dict_2 and int(time%2) == 0:
        # reached a "stable" solution
        write_output(state_dict, row_total, column_total)
    else:
        # move on to the next time step
        state_dict_2 = state_dict_1.copy()
        state_dict_1 = state_dict.copy()
        state_dict = {}








