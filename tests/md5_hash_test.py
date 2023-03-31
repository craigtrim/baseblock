# -*- coding: utf-8 -*-


from baseblock import BaseObject


def test_inversions():

    input_text = 'What is a typical day in your life like?'

    assert BaseObject.md5hash(
        input_text) == 168613937257915006789722958274892615824


def main():
    test_inversions()


if __name__ == '__main__':
    main()
