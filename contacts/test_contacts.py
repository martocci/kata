def test_add_contact():
    '''
    When a single contact is inserted, the length of the list returns goes up by one
    '''
    from contacts import add_contact as addcon

    test_list = ['a']
    assert len(test_list) + 1 == len(addcon(test_list,'b'))


def test_parse_row_partial():
    '''
    When a string has a partial command, the command booleans should be set correctly,
       and the data should be returned
    '''

    from contacts import parse_row as parserow

    is_add, is_count, is_partial, data = parserow('partial abc')
    assert is_add is False
    assert is_partial is True
    assert is_count is False
    assert data == 'abc'


def test_parse_row_partial_with_spaces():
    '''
    When a string has extra whitespace, the data and commands should be returned correctly.
    '''

    from contacts import parse_row as parserow

    is_add, is_count, is_partial, data = parserow('   partial    abc    ')
    assert is_add is False
    assert is_partial is True
    assert is_count is False
    assert data == 'abc'

def test_parse_row_add():
    '''
    When a string has a add command, the command booleans should be set correctly,
       and the data should be returned
    '''

    from contacts import parse_row as parserow

    is_add, is_count, is_partial, data = parserow('add abc')
    assert is_add is True
    assert is_partial is False
    assert is_count is False
    assert data == 'abc'

def test_parse_row_count():
    '''
    When a string doesn't have a partial or add command, the command booleans should be set correctly,
       and the data should be returned
    '''

    from contacts import parse_row as parserow

    is_add, is_count, is_partial, data = parserow('2')
    assert is_add is False
    assert is_partial is False
    assert is_count is True
    assert data == None



