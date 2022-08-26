from typing import Text
from baseblock import TextUtils

input_text = "the quick brown fox jumped over the lazy dog"


def test_title_case():
    result = TextUtils.title_case(input_text)
    print(result)

    assert result
    assert type(result) == str

    assert result == "The Quick Brown Fox Jumped Over the Lazy Dog"

    assert TextUtils.title_case("IBM") == "IBM"


def test_sentence_case():
    result = TextUtils.sentence_case(input_text)
    print(result)

    assert result
    assert type(result) == str

    assert result == "The quick brown fox jumped over the lazy dog"


def test_lower_case():
    result = TextUtils.lower_case(input_text)
    print(result)

    assert result
    assert type(result) == str

    assert result == "the quick brown fox jumped over the lazy dog"


def test_update_determiners():
    assert TextUtils.update_determiners(
        "this is a umbrella") == "this is an umbrella"

    assert TextUtils.update_determiners(
        "a incredible contributor") == "an incredible contributor"

    assert TextUtils.update_determiners(
        'Such a "Insanely Productive" work ethic') == 'Such an "Insanely Productive" work ethic'

    assert TextUtils.update_determiners(
        "A incredible contributor") == "An incredible contributor"


def test_subsumes():

    results = TextUtils.find_subsumed_tokens(
        ['alpha beta gamma', 'beta gamma', 'gamma'])

    assert results == ['beta gamma', 'gamma']


def test_is_punctuation():

    # this function tests single chars only
    assert TextUtils.is_punctuation('!')
    assert not TextUtils.is_punctuation('a')

    # any input > 1 is automatically false
    assert not TextUtils.is_punctuation('alpha')
    assert not TextUtils().is_punctuation('alpha!')


def test_has_punctuation():

    # return True if any punctuation exists
    assert TextUtils.has_punctuation('!')
    assert not TextUtils.has_punctuation('a')

    # return True if any punctuation exists
    assert not TextUtils.has_punctuation('alpha')
    assert TextUtils().has_punctuation('alpha!')


def test_remove_punctuation():

    # return True if any punctuation exists
    assert TextUtils.remove_punctuation('!') == ''
    assert TextUtils.remove_punctuation('a') == 'a'

    # return True if any punctuation exists
    assert TextUtils.remove_punctuation('alpha') == 'alpha'
    assert TextUtils.remove_punctuation('alpha!') == 'alpha'

    # demonstrate whitespace handling
    assert TextUtils.remove_punctuation(
        'alpha beta gamma') == 'alpha beta gamma'

    assert TextUtils.remove_punctuation(
        'alpha...beta gamma') == 'alphabeta gamma'

    assert TextUtils.remove_punctuation(
        'alpha ... beta gamma') == 'alpha  beta gamma'
