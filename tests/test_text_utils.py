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
