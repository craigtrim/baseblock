# -*- coding: utf-8 -*-
from baseblock import CryptoBase


def test_component():

    crypt = CryptoBase()

    input_text = 'This is only a drill.'
    x = crypt.encrypt_str(input_text)
    y = crypt.decrypt_str(x)

    assert y == input_text


def main():
    test_component()


if __name__ == '__main__':
    main()
