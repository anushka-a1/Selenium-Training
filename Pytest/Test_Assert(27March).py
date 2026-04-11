# creating a function to test if the two strings are equal
""" def test_assert_equal():
    assert '4' == '5'

def test_assert_not_equal():
    assert 'Hi' != 'Hello'

def test_assert_equal():
    assert '4' == '4'

def test_assert_not_equal():
    assert '4' != '5'
 """

# checking greater than or equal to
""" def test_assert_equal():
    assert 10 >= 10
 """
""" def test_assert_equal():
    assert 10 <= 9
 """

# using membership operator
""" def test_assert_equal():
    l=[1,2,3,4,5]
    assert 4 in l
 """
def test_assert_equal():
    l=['apple','banana','cherry','mango','orange']
    assert 'apple' in l

def test_assert_not_equal():
    l=['apple','banana','cherry','mango','orange']
    assert 'pineapple' not in l