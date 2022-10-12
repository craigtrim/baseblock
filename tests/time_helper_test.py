from baseblock import Enforcer
from baseblock import TimeHelper


def test_ts_to_dict():

    d = TimeHelper.ts_to_dict(1660318448.491499)
    Enforcer.is_dict(d)

    assert d == {
        'day': 12,
        'dayname': 'Friday',
        'hour': 8,
        'iso': '2022-08-12T08:34:08',
        'minute': 34,
        'month': 8,
        'second': 8,
        'year': 2022
    }


def main():
    test_ts_to_dict()


if __name__ == "__main__":
    main()
