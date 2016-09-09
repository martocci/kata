import re

def add_contact(contact_list, contact):
    '''
    Append to the list of contacts
    returns new list
    '''

    return contact_list + [contact]

def parse_row(row_string):
    '''
    Figures out whether the row is an "add" or "partial" command or the initial row count
    Returns the boolean add or partial and the associated data
    '''

    row_list = row_string.split()

    is_partial, is_add, is_count = False, False, False
    data = None
    if row_list[0] == "partial":
        is_partial = True
        data = row_list[1]
    elif row_list[0] == "add":
        is_add = True
        data = row_list[1]
    elif row_list[0].isdigit():
        is_count = True

    return is_add, is_count, is_partial, data



