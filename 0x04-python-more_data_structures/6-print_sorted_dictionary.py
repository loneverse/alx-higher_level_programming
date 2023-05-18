#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.items())
# sorted_dict
    for k, v in sorted_dictionary:
        print('{0}: {1}'.format(k, v))
