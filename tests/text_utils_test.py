# -*- coding: utf-8 -*-
from mimetypes import common_types
from baseblock import TextUtils

input_text = 'the quick brown fox jumped over the lazy dog'


def test_is_equal():
    input_1 = """
+----+----------+--------------------------+--------------+
|    | Parent   | Child                    | Confidence   |
|----+----------+--------------------------+--------------|
|  0 | network  | mitchellusatoday network |              |
|  1 | platform | people's platform        |              |
|  2 | deal     | new deal                 |              |
|  3 | new deal | green new deal           |              |
|  4 | discus   | article discus           |              |
|  5 | energy   | green energy             |              |
+----+----------+--------------------------+--------------+
    """

    input_2 = """
            +----+----------+--------------------------+--------------+
            |    | Parent   | Child                    | Confidence   |
            |----+----------+--------------------------+--------------|

            |  0 | network  | mitchellusatoday network |              |
            |  1 | platform | people's platform        |              |

            |  2 | deal     | new deal                 |              |
            |  3 | new deal | green new deal           |              |

            |  4 | discus   | article discus           |              |
            |  5 | energy   | green energy             |              |
            +----+----------+--------------------------+--------------+
    """.strip()

    assert TextUtils.is_equal(input_1, input_2)

    # sanity checks
    assert TextUtils.is_equal(input_1, input_1)
    assert TextUtils.is_equal(input_2, input_2)


def test_most_similar_phrase_1():

    tokens_1 = ['where', 'can', 'I', 'find', 'the', 'library']
    tokens_2 = ['I', 'understand', 'you',
                'want', 'to', 'find', 'the', 'library']

    results = TextUtils.most_similar_phrase(
        tokens_1=tokens_1,
        tokens_2=tokens_2,
        window_size=4,
        score_threshold=0.70,
        debug=False)

    assert results == {
        0.75: {
            'tokens_1': 'can i find the',
            'tokens_2': 'want to find the'
        },
        0.929: {
            'tokens_1': 'i find the library',
            'tokens_2': 'to find the library',
        }
    }


def test_most_similar_phrase_2():

    tokens_1 = ['where', 'can', 'I', 'find', 'the', 'library']
    tokens_2 = ['I', 'understand', 'you',
                'want', 'to', 'find', 'the', 'library']

    results = TextUtils.most_similar_phrase(
        tokens_1=tokens_1,
        tokens_2=tokens_2,
        window_size=6,
        score_threshold=0.70,
        debug=False)

    assert results == {
        0.824: {
            'tokens_1': 'where can i find the library',
            'tokens_2': 'you want to find the library'
        }
    }


def test_sliding_window():

    tokens = input_text.split()
    assert tokens == [
        'the',
        'quick',
        'brown',
        'fox',
        'jumped',
        'over',
        'the',
        'lazy',
        'dog'
    ]

    bigrams = TextUtils.sliding_window(tokens=tokens, window_size=2)
    assert bigrams == [
        ['the', 'quick'],
        ['quick', 'brown'],
        ['brown', 'fox'],
        ['fox', 'jumped'],
        ['jumped', 'over'],
        ['over', 'the'],
        ['the', 'lazy'],
        ['lazy', 'dog']
    ]

    trigrams = TextUtils.sliding_window(tokens=tokens, window_size=3)
    assert trigrams == [
        ['the', 'quick', 'brown'],
        ['quick', 'brown', 'fox'],
        ['brown', 'fox', 'jumped'],
        ['fox', 'jumped', 'over'],
        ['jumped', 'over', 'the'],
        ['over', 'the', 'lazy'],
        ['the', 'lazy', 'dog']
    ]

    quadgrams = TextUtils.sliding_window(tokens=tokens, window_size=4)
    assert quadgrams == [
        ['the', 'quick', 'brown', 'fox'],
        ['quick', 'brown', 'fox', 'jumped'],
        ['brown', 'fox', 'jumped', 'over'],
        ['fox', 'jumped', 'over', 'the'],
        ['jumped', 'over', 'the', 'lazy'],
        ['over', 'the', 'lazy', 'dog']
    ]


def test_remove_duplicated_phrases():

    text_1 = "The earliest known age of fossils is 3.7 billion years old. Some would argue that life arose within a few hundred million years of Earth's origin, perhaps as early as 4.2 billion years ago, but the violent bombardment and geological activity of Earth's first few hundred million years have obliterated any firm evidence of such early life. Nevertheless, even the 3.7 - billion - year age of the earliest fossils shows that life has been a feature of Planet Earth for most of its history."

    text_2 = 'The earliest known age of fossils is 3.7 billion years old.'

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

    assert result == 'The Quick Brown Fox Jumped Over the Lazy Dog'

    assert TextUtils.title_case('IBM') == 'IBM'


def test_sentence_case():
    result = TextUtils.sentence_case(input_text)
    print(result)

    assert result
    assert type(result) == str

    assert result == 'The quick brown fox jumped over the lazy dog'


def test_lower_case():
    result = TextUtils.lower_case(input_text)
    print(result)

    assert result
    assert type(result) == str

    assert result == 'the quick brown fox jumped over the lazy dog'


def test_update_determiners():
    assert TextUtils.update_determiners(
        'this is a umbrella') == 'this is an umbrella'

    assert TextUtils.update_determiners(
        'a incredible contributor') == 'an incredible contributor'

    assert TextUtils.update_determiners(
        'Such a "Insanely Productive" work ethic') == 'Such an "Insanely Productive" work ethic'

    assert TextUtils.update_determiners(
        'A incredible contributor') == 'An incredible contributor'


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
        'alpha ... beta gamma') == 'alpha beta gamma'


def test_chunk_list():

    assert TextUtils.chunk_list([
        'input sentence 1',
        'input sentence 2',
        'input sentence 3',
        'input sentence 4',
        'input sentence 5',
    ], max_chunk_size=50) == [
        'input sentence 1  input sentence 2  input sentence 3  input sentence 4',
        'input sentence 5'
    ]

    results = TextUtils.chunk_list([
        'Reinforcing the ETH narrative handled well given its on-chain, auditable properties.',
        'Of course, DeFi comes with its own risks like smart contract exploits. This could put more scrutiny on how different decentralized applications are managing their protocol risks, given the recent proliferation of alternative layer-1 blockchains saturating the marketplace. Many in the crypto community have questioned the need for additional L1s.',
        "Rules-based margining needs to account for the fact that volatility of certain digital assets can be between 50-200%, affecting their true liquidity. Ethereum's successful merge of consensus and execution layers has also strengthened the case for ambitious future upgrades, despite the trend towards core protocol ossification.",
        'In our view, this supports the narrative for Ethereum as a leader in a multichain world. Nearly all networks are competing for the same pool of users and capital.',
        "Some ecosystems are doing better than others, and we believe user and developer activity will aggregate to a smaller number of chains in 2023 compared to 2022. Ethereum's dominance could still be challenged in other ways, as the network relies on layer-2 scaling solutions to extend its blockspace, which have their own set of risks.",
        'This includes centralized 50 sequencers, a lack of fraud proofs, and a lack of cross L2 interoperability, to name a few. Growth of a decentralized future The movement towards self-custody and decentralized finance (DeFi) protocols (i.e. decentralized exchanges or DEXs) will likely accelerate after the developments in 4Q22. Many industry players believe that the transgressions in the crypto space in 2022 were concentrated among CeFi (centralized finance) or CeDeFi (a combination of both CeFi and DeFi) entities, such as Celsius, Three Arrows Capital (3AC), and FTX.',
    ], max_chunk_size=750)

    for result in results:
        print(result)
        print('-'*50)


def test_cartesian_bigrams():
    tags = ['Light', 'Lighting', 'Purple', 'People', 'Person',
            'Laser', 'Shoe', 'Face', 'Head', 'Graduation']

    results = TextUtils.cartesian_bigrams(tags)

    for result in results:
        inverse = [result[1], result[0]]
        assert inverse not in results

    assert TextUtils.cartesian_bigrams(tags) == [
        ['Face', 'Head'],
        ['Face', 'Shoe'],
        ['Graduation', 'Face'],
        ['Graduation', 'Head'],
        ['Graduation', 'Laser'],
        ['Graduation', 'Light'],
        ['Graduation', 'Lighting'],
        ['Graduation', 'People'],
        ['Graduation', 'Person'],
        ['Graduation', 'Purple'],
        ['Graduation', 'Shoe'],
        ['Head', 'Shoe'],
        ['Laser', 'Face'],
        ['Laser', 'Head'],
        ['Laser', 'Light'],
        ['Laser', 'Shoe'],
        ['Light', 'Face'],
        ['Light', 'Head'],
        ['Light', 'Shoe'],
        ['Lighting', 'Face'],
        ['Lighting', 'Head'],
        ['Lighting', 'Laser'],
        ['Lighting', 'Light'],
        ['Lighting', 'People'],
        ['Lighting', 'Person'],
        ['Lighting', 'Purple'],
        ['Lighting', 'Shoe'],
        ['People', 'Face'],
        ['People', 'Head'],
        ['People', 'Laser'],
        ['People', 'Light'],
        ['People', 'Person'],
        ['People', 'Purple'],
        ['People', 'Shoe'],
        ['Person', 'Face'],
        ['Person', 'Head'],
        ['Person', 'Laser'],
        ['Person', 'Light'],
        ['Person', 'Purple'],
        ['Person', 'Shoe'],
        ['Purple', 'Face'],
        ['Purple', 'Head'],
        ['Purple', 'Laser'],
        ['Purple', 'Light'],
        ['Purple', 'Shoe']
    ]


def test_cartesian_trigrams():
    tags = ['Light', 'Lighting', 'Purple', 'People', 'Person',
            'Laser', 'Shoe', 'Face', 'Head', 'Graduation']

    results = TextUtils.cartesian_trigrams(tags)

    for result in results:
        print(result)


def test_cartesian_quadgrams():
    tags = ['Light', 'Lighting', 'Purple', 'People', 'Person',
            'Laser', 'Shoe', 'Face', 'Head', 'Graduation']

    results = TextUtils.cartesian_quadgrams(tags)

    for result in results:
        print(result)


def main():
    test_chunk_list()


if __name__ == '__main__':
    main()
