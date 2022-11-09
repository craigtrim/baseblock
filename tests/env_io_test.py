# -*- coding: utf-8 -*-


import os

from baseblock import EnvIO


def test_as_str():

    # init env ...
    os.environ['alpha'] = '1'
    os.environ['beta'] = '2'
    os.environ['gamma'] = '3'

    assert EnvIO.as_str('alpha', 'beta', 'gamma') == '1'

    # 'alpha2' doesn't exist; so use 'beta'
    assert EnvIO.as_str('alpha2', 'beta', 'gamma') == '2'

    # 'alpha2' and 'beta2' don't exist; so use 'gamma'
    assert EnvIO.as_str('alpha2', 'beta2', 'gamma') == '3'

    # no env vars exist; return None
    assert not EnvIO.as_str('alpha2', 'beta2', 'gamma2')

    # ... clean up env
    del os.environ['alpha']
    del os.environ['beta']
    del os.environ['gamma']


def main():
    test_as_str()


if __name__ == '__main__':
    main()
