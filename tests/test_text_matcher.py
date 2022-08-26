from baseblock import TextMatcher

input_text_1 = "the quick brown fox jumped over the lazy dog"


def test_exists():

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


def test_replace():

    tm = TextMatcher
    assert tm

    # demontrate bigram match
    assert tm.replace(input_text=input_text_1,
                      old_value='brown fox',
                      new_value='purple elephant',
                      case_sensitive=False) == "the quick purple elephant jumped over the lazy dog"

    # demonstrate that only 'whole-string' matches are performed
    assert tm.replace(input_text="the fox and the fox together outfoxed every foxy fox that foxed foxily",
                      old_value='fox',
                      new_value='entity_fox',
                      case_sensitive=False) == "the entity_fox and the entity_fox together outfoxed every foxy entity_fox that foxed foxily"


def test_coords():

    tm = TextMatcher
    assert tm

    x, y = tm.coords(input_text=input_text_1,
                     value='quick')
    print(f"X,Y: {x},{y}: ({input_text_1[x:y]})")
    assert input_text_1[x:y] == 'quick'

    x, y = tm.coords(input_text=input_text_1,
                     value='the')
    print(f"X,Y: {x},{y}: ({input_text_1[x:y]})")
    assert input_text_1[x:y] == 'the'

    x, y = tm.coords(input_text=input_text_1,
                     value='dog')
    print(f"X,Y: {x},{y}: ({input_text_1[x:y]})")
    assert input_text_1[x:y] == 'dog'


def main():
    test_exists()
    test_replace()
    test_coords()


if __name__ == "__main__":
    main()
