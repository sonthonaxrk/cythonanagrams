import pytest
from anagrams_finder import PyAnagramFinder


def test_single_word():
    finder = PyAnagramFinder()
    finder.add_word('a')
    assert finder.search() == set()


def test_basic_match():
    finder = PyAnagramFinder()
    finder.add_word('ab')
    finder.add_word('ba')
    assert finder.search() == {'ab', 'ba'}


def test_multiple_matchings():
    finder = PyAnagramFinder()
    finder.add_word('eat')
    finder.add_word('my')
    finder.add_word('tea')
    assert finder.search() == {'eat', 'tea'}


@pytest.mark.parametrize(
    'test_input,expected', 
    [
       ('the quick brown fox', set()),
       ('eat my tea', {'eat', 'tea'}),
       ('do or door no no', set()),
       ('pots stop pots spot stop', {'pots', 'stop', 'spot'}),
        (
            'on pots no stop eat ate pots spot stop tea',
            {'on', 'no', 'pots', 'stop', 'spot', 'eat', 'ate', 'tea'}
        )
    ]
)
def test_multiple_matchings(test_input, expected):
    finder = PyAnagramFinder()

    for word in test_input.split(' '):
        finder.add_word(word)

    assert finder.search() == expected


if __name__ == '__main__':
    pytest.main()
