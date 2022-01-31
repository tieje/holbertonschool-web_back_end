#!/usr/bin/python3
'''10. Duck typing - first element of a sequence'''
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
