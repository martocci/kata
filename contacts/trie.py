indices = {
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z',
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
}

def parse_row(row_string):
    '''
    Figures out whether the row is an "add" or "partial" command or the initial row count
    Returns the boolean add or partial and the associated data
    '''

    row_list = row_string.split()

    is_partial, is_add, is_count = False, False, False
    data = None
    if row_list[0] == "find":
        is_partial = True
        data = row_list[1]
    elif row_list[0] == "add":
        is_add = True
        data = row_list[1]
    elif row_list[0].isdigit():
        is_count = True
        data = row_list[0]

    return is_add, is_count, is_partial, data

class vertex(object):

    def __init__(self):
        self.partials = 0
        self.edges = 26*[None]

def add_contact(vert, contact):
    '''
    Recursively add vertices for each letter in "contact"
    '''
    pass
    if contact == "":
        vert.partials = vert.partials + 1
    #if contact != "":
    else:
        vert.partials = vert.partials + 1
        k = contact[0]
        contact = contact[1:]
        k_ind = indices[k]
        if vert.edges[k_ind] == None:
            vert.edges[k_ind] = vertex()
        add_contact(vert.edges[k_ind], contact)

def count_partials(vertex, word):
    '''
    Get the count of the number of contacts starting with a given partial
    '''
    pass

    if word == '':
        return vertex.partials
    else:
        k_ind = indices[word[0]]
        if vertex.edges[k_ind] is None:
            return 0
        else:
            word = word[1:]
            return count_partials(vertex.edges[k_ind], word)


# Read file
import fileinput
import sys

new_trie = vertex()

file = '/Users/kmartocci/github_dir/kata/contacts/test_data.txt'
with open(file) as f:

  for line in f:

#for line in sys.stdin:
        print(line)
        is_add, is_count, is_partial, data = parse_row(line)

        if is_count:
            row_count = data
        elif is_add:
            add_contact(new_trie, data)
        elif is_partial:
            partial_count = count_partials(new_trie, data)
            print(partial_count)



