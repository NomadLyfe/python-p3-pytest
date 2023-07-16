#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    '''in bool_functions, function "return_true" returns True.'''
    assert return_not_none() != None
