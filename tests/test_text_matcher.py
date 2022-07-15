from baseblock import TextMatcher

input_text_1 = "the quick brown fox jumped over the lazy dog"


def test_matcher():

    tm = TextMatcher
    assert tm

    assert tm.exists("the", input_text_1)
    assert tm.exists("fox", input_text_1)
    assert tm.exists("dog", input_text_1)

    assert not tm.exists("do", input_text_1)  # $dog
    assert not tm.exists("he", input_text_1)  # ^the
    assert not tm.exists("own", input_text_1)  # brown
    assert not tm.exists("la", input_text_1)  # lazy
    assert not tm.exists("jump", input_text_1)  # jumped


def main():
    test_matcher()


if __name__ == "__main__":
    main()
