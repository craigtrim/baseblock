# -*- coding: utf-8 -*-


import os

from baseblock import Enforcer


def test_enforcer():

    Enforcer.is_dict_of_list_of_strs({
        'a': [
            'alpha',
            'beta',
        ],
        'b': [
            'gamma',
            'delta',
        ]
    })

    Enforcer.is_dict_of_list_of_ints({
        'a': [
            1,
            2
        ],
        'b': [
            3,
            4
        ]
    })

    Enforcer.is_dict_of_list_of_floats({
        'a': [
            0.1,
            1.0,
        ],
        'b': [
            1.1,
            2.0,
        ]
    })

    Enforcer.is_dict_of_list_of_tuples({
        'a': [
            (0, 1),
            (2, 3),
        ],
        'b': [
            (3, 4),
            (5, 6),
        ]
    })

    Enforcer.is_dict_of_list_of_dicts({
        'a': [
            {'x': []},
            {'y': []}
        ],
        'b': [
            {'x': []},
            {'y': []}
        ]
    })

    Enforcer.is_dict_of_list_of_typed_dicts({
        'a': [
            {'x': [], 'y': [], 'z': []},
            {'x': [], 'y': [], 'z': []},
        ],
        'b': [
            {'x': [], 'y': [], 'z': []},
            {'x': [], 'y': [], 'z': []},
        ]
    }, ['x', 'y', 'z'])


def main():
    test_enforcer()


if __name__ == '__main__':
    main()
