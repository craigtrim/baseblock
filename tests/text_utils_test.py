from mimetypes import common_types
from baseblock import TextUtils

input_text = "the quick brown fox jumped over the lazy dog"


def test_remove_duplicated_phrases():

    text_1 = "The earliest known age of fossils is 3.7 billion years old. Some would argue that life arose within a few hundred million years of Earth's origin, perhaps as early as 4.2 billion years ago, but the violent bombardment and geological activity of Earth's first few hundred million years have obliterated any firm evidence of such early life. Nevertheless, even the 3.7 - billion - year age of the earliest fossils shows that life has been a feature of Planet Earth for most of its history."

    text_2 = "The earliest known age of fossils is 3.7 billion years old."

    text_1 = TextUtils.remove_duplicated_phrases(
        text_1=text_1,
        text_2=text_2)

    assert text_1 == "Some would argue that life arose within a few hundred million years of Earth's origin, perhaps as early as 4.2 billion years ago, but the violent bombardment and geological activity of Earth's first few hundred million years have obliterated any firm evidence of such early life. Nevertheless, even the 3.7 - billion - year age of the earliest fossils shows that life has been a feature of Planet Earth for most of its history."


def test_longest_common_phrase_1():

    tokens_1 = ['what', 'is', 'the', 'earliest',
                'known', 'age', 'of', 'fossils', '?']

    tokens_2 = ['the', 'earliest', 'known', 'age', 'of',
                'fossils', 'is', '3.7', 'billion', 'years', 'old', '.']

    common_tokens = TextUtils.longest_common_phrase(
        tokens_1=tokens_1,
        tokens_2=tokens_2)

    assert common_tokens == ['the', 'earliest',
                             'known', 'age', 'of', 'fossils']


def test_longest_common_phrase_2():

    tokens_1 = ['ask', 'me', 'a', 'random', 'question']

    tokens_2 = ['what', 'is', 'a', 'watt']

    common_tokens = TextUtils.longest_common_phrase(
        tokens_1=tokens_1,
        tokens_2=tokens_2)

    assert not common_tokens


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


def main():
    test_longest_common_phrase_2()


if __name__ == "__main__":
    main()
