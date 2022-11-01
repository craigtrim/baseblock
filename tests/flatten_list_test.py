# -*- coding: utf-8 -*-
from baseblock import flatten_list


def test_flatten_list():
    input_list = [
        [
            ['a'],
            ['b'],
            ['c']
        ]
    ]

    output_list = flatten_list(input_list)

    assert output_list == [
        'a',
        'b',
        'c',
    ]


def main():
    test_flatten_list()


if __name__ == '__main__':
    main()
