def test_parse_row_partial():
    '''
    When a string has a partial command, the command booleans should be set correctly,
       and the data should be returned
    '''

    from trie import parse_row as parserow

    is_add, is_count, is_partial, data = parserow('find abc')
    assert is_add is False
    assert is_partial is True
    assert is_count is False
    assert data == 'abc'


def test_parse_row_partial_with_spaces():
    '''
    When a string has extra whitespace, the data and commands should be returned correctly.
    '''

    from trie import parse_row as parserow

    is_add, is_count, is_partial, data = parserow('   find    abc    ')
    assert is_add is False
    assert is_partial is True
    assert is_count is False
    assert data == 'abc'

def test_parse_row_add():
    '''
    When a string has a add command, the command booleans should be set correctly,
       and the data should be returned
    '''

    from trie import parse_row as parserow

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

    from trie import parse_row as parserow

    is_add, is_count, is_partial, data = parserow('2')
    assert is_add is False
    assert is_partial is False
    assert is_count is True
    assert data == data

def test_trie_initialization():
    '''
    When a trie is initialized, the starting edges list should be 26 Nones
       & the prefix count should be 0
    '''

    from trie import vertex

    new_trie = vertex()

    assert new_trie.partials == 0
    assert len(new_trie.edges) == 26
    assert new_trie.edges[0] == None
    assert new_trie.edges[10] == None
    assert new_trie.edges[19] == None
    assert new_trie.edges[25] == None

def test_letter_indices():
    '''
    When a letter is given, then the corresponding integer should be in letter_indices
    '''
    from trie import indices as ind

    assert ind['a'] == 0
    assert ind[1] == 'b'

def test_add_contact_one_letter():
    '''
    When a contact that is one letter long is added,
       the edge should have a prefix total = 1 and one edge
    '''
    from trie import vertex, add_contact

    new_trie = vertex()
    add_contact(new_trie, 'a')

    # first (null) vertex
    assert new_trie.partials == 1

    # first letter = a
    assert new_trie.edges[0] is not None

    # first letter != b
    assert new_trie.edges[1] is None

    # There is one partial = 'a'
    assert new_trie.edges[0].partials == 1


def test_add_contact_two_letters():
    '''
    When a contact that is two letters long is added,
       the last edge should have a prefix total = 1 and one edge
    '''
    from trie import vertex, add_contact

    new_trie = vertex()
    add_contact(new_trie, 'ab')

    # first letter = 'a'
    assert new_trie.edges[0] is not None

    # There is one partial that starts with 'a'
    assert new_trie.edges[0].partials == 1

    # first 2 letters = 'ab'
    assert new_trie.edges[0].edges[1] is not None

    # There is 1 partial that is 'ab'
    assert new_trie.edges[0].edges[1].partials == 1

    # first letter is not 'b'
    assert new_trie.edges[1] is None


def test_add_contact_four_letters():
    '''
    When a contact that is four letters long is added,
       the last edge should have a prefix total = 1 and one edge
    '''
    from trie import vertex, add_contact

    new_trie = vertex()
    add_contact(new_trie, 'abcd')

    # first letter = 'a'
    assert new_trie.edges[0] is not None

    # first letter = 'ab'
    assert new_trie.edges[0].edges[1] is not None

    # first letter = 'abc'
    assert new_trie.edges[0].edges[1].edges[2] is not None

    # first letter = 'abcd'
    assert new_trie.edges[0].edges[1].edges[2].edges[3] is not None

    # There is one partial that starts with 'a'
    assert new_trie.edges[0].partials == 1

    # There is 1 partial that is 'ab'
    assert new_trie.edges[0].edges[1].partials == 1

    # There is 1 partial that is 'abc'
    assert new_trie.edges[0].edges[1].edges[2].partials == 1

    # There is 1 partial that is 'abcd'
    assert new_trie.edges[0].edges[1].edges[2].edges[3].partials == 1

def test_add_three_contacts_four_letters():
    '''
    When three overlapping contact that is four letters long is added,
       the last edge should have a prefix total = 1 and one edge
    '''
    from trie import vertex, add_contact

    new_trie = vertex()
    add_contact(new_trie, 'abcd')
    add_contact(new_trie, 'abde')
    add_contact(new_trie, 'acde')

    # There are 3 partials that starts with 'a'
    assert new_trie.edges[0].partials == 3

    # There are 2 partials that is 'ab'
    assert new_trie.edges[0].edges[1].partials == 2

    # There is 1 partial that is 'ac'
    assert new_trie.edges[0].edges[2].partials == 1

    # There is 1 partial that is 'abcd'
    assert new_trie.edges[0].edges[1].edges[2].edges[3].partials == 1

    # There is 1 partial that is 'abde'
    assert new_trie.edges[0].edges[1].edges[3].edges[4].partials == 1

    # There is 1 partial that is 'acde'
    assert new_trie.edges[0].edges[2].edges[3].edges[4].partials == 1

def test_count_partials_one_letter_once():
    '''
    Count how many contacts that start with 'a' if one 'a' is inserted
    '''

    from trie import vertex, add_contact, count_partials

    new_trie = vertex()
    add_contact(new_trie, 'a')

    assert count_partials(new_trie, 'a') == 1

def test_count_one_letter_many():
    '''
    Count how many contacts that start with 'a' if 5 'a's are inserted
    '''

    from trie import vertex, add_contact, count_partials

    new_trie = vertex()
    add_contact(new_trie, 'a')
    add_contact(new_trie, 'a')
    add_contact(new_trie, 'a')
    add_contact(new_trie, 'a')
    add_contact(new_trie, 'a')

    assert count_partials(new_trie, 'a') == 5

def test_count_partials_one_letter_many_words():
    '''
    Count how many contacts that start with 'a' if many different
        contacts starting with 'a' are inserted
    '''

    from trie import vertex, add_contact, count_partials

    new_trie = vertex()
    add_contact(new_trie, 'abc')
    add_contact(new_trie, 'asdf')
    add_contact(new_trie, 'art')
    add_contact(new_trie, 'attt')

    assert count_partials(new_trie, 'a') == 4

def test_count_partials_three_letter_many_words():
    '''
    Count how many contacts that start with 'abc' if many different
        contacts starting with 'abc' are inserted
    '''

    from trie import vertex, add_contact, count_partials

    new_trie = vertex()
    add_contact(new_trie, 'abc')
    add_contact(new_trie, 'abcsdf')
    add_contact(new_trie, 'abcrt')
    add_contact(new_trie, 'abcttt')

    assert count_partials(new_trie, 'a') == 4





