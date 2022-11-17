def positive_negative_number(a):
    x = str(a)
    if x.isalpha == True:
        return 'not a number'
    else:
        if x.startswith('-'):
            return 'negative'
        elif x == '0':
            return 'zero'
        else:
            return 'positive'

def test_pn():
    assert positive_negative_number(-1) == 'negative'
    assert positive_negative_number(8) == 'positive'
    assert positive_negative_number(0) == 'zero'
    assert positive_negative_number('hello') == 'not a number'

def to_power(a, b):
    '''function returning a to the power of b
    >>> to_power(4, 2)
    16
    >>> to_power(11, 3)
    1331
    >>> to_power(0, 0)
    1
    
    '''
    return a**b

def try_modulo(a, b):
    '''function returning remainder after number division
    >>> try_modulo(14, 3)
    2
    >>> try_modulo(8, 5)
    3
    >>> try_modulo(10, 1)
    0
    '''
    return a % b

    #>>> try_modulo(4, 0)
    #ZeroDivisionError

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    test_pn()
     