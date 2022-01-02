"""Spell a name using a phonetic code."""

import string
import unittest

NATO = ['ALPHA',
        'BRAVO',
        'CHARLIE',
        'DELTA',
        'ECHO',
        'FOXTROT',
        'GOLF',
        'HOTEL',
        'INDIA',
        'JULIETT',
        'KILO',
        'LIMA',
        'MIKE',
        'NOVEMBER',
        'OSCAR',
        'PAPA',
        'QUEBEC',
        'ROMEO',
        'SIERRA',
        'TANGO',
        'UNIFORM',
        'VICTOR',
        'WHISKEY',
        'XRAY',
        'YANKEE',
        'ZULU']
"""Words in the NATO phonetic code."""

def spell(name, words = NATO):
    """Spell name using the words in words.

    Args:
        name: String name.
        words: Optional list of words starting with each letter of the alphabet
            with which to spell name.
    Returns:
        List of string words to spell name.
    """
    if not isinstance(name, str):
        raise TypeError('name must be a non-empty string of letters.')
    if len(name) <= 0:
        raise ValueError('name must be a non-empty string of letters.')

    name = name.strip().lower()
    letter_map = dict((word[0].lower(), word) for word in words
                      if isinstance(word, str) and (len(word) > 0))
    result = []
    for letter in name:
        if letter in letter_map:
            result.append(letter_map[letter])
        else:
            raise ValueError('name must be a non-empty string of letters.')
    return result


class _UnitTest(unittest.TestCase):
    def test_NATO(self):
        """Test the words in the NATO phonetic code."""
        self.assertEqual(len(NATO), 26)
        for letter, word in zip(string.ascii_uppercase, NATO):
            self.assertEqual(word, word.strip())
            self.assertEqual(word, word.upper())
            self.assertGreater(len(word), 0)
            self.assertTrue(word.startswith(letter))

    def test_spell(self):
        """Test spelling a name."""
        for value in [None, 42, []]:
            self.assertRaises(TypeError, spell, value)
        for value in ['', '8oo', '*ab']:
            self.assertRaises(ValueError, spell, value)
        for value, expected in [
            ('Ashcraft', ['ALPHA', 'SIERRA', 'HOTEL', 'CHARLIE', 'ROMEO', 'ALPHA', 'FOXTROT', 'TANGO']),
            ('Ashcroft', ['ALPHA', 'SIERRA', 'HOTEL', 'CHARLIE', 'ROMEO', 'OSCAR', 'FOXTROT', 'TANGO']),
            ('Deusen', ['DELTA', 'ECHO', 'UNIFORM', 'SIERRA', 'ECHO', 'NOVEMBER']),
            ('Gutierrez', ['GOLF', 'UNIFORM', 'TANGO', 'INDIA', 'ECHO', 'ROMEO', 'ROMEO', 'ECHO', 'ZULU']),
            ('Honeyman', ['HOTEL', 'OSCAR', 'NOVEMBER', 'ECHO', 'YANKEE', 'MIKE', 'ALPHA', 'NOVEMBER']),
            ('Jackson', ['JULIETT', 'ALPHA', 'CHARLIE', 'KILO', 'SIERRA', 'OSCAR', 'NOVEMBER']),
            ('Lee', ['LIMA', 'ECHO', 'ECHO']),
            ('Pfister', ['PAPA', 'FOXTROT', 'INDIA', 'SIERRA', 'TANGO', 'ECHO', 'ROMEO']),
            ('Rubin', ['ROMEO', 'UNIFORM', 'BRAVO', 'INDIA', 'NOVEMBER']),
            ('Robert', ['ROMEO', 'OSCAR', 'BRAVO', 'ECHO', 'ROMEO', 'TANGO']),
            ('Rupert', ['ROMEO', 'UNIFORM', 'PAPA', 'ECHO', 'ROMEO', 'TANGO']),
            ('Tymczak', ['TANGO', 'YANKEE', 'MIKE', 'CHARLIE', 'ZULU', 'ALPHA', 'KILO']),
            ('VanDeusen', ['VICTOR', 'ALPHA', 'NOVEMBER', 'DELTA', 'ECHO', 'UNIFORM', 'SIERRA', 'ECHO', 'NOVEMBER']),
            ('Washington', ['WHISKEY', 'ALPHA', 'SIERRA', 'HOTEL', 'INDIA', 'NOVEMBER', 'GOLF', 'TANGO', 'OSCAR', 'NOVEMBER'])]:
            self.assertEqual(spell(value), expected)
            self.assertEqual(spell(value.lower()), expected)
            self.assertEqual(spell(value.title()), expected)
            self.assertEqual(spell(value.upper()), expected)
            self.assertEqual(spell(value, NATO), expected)
            self.assertEqual(spell(value.lower(), NATO), expected)
            self.assertEqual(spell(value.title(), NATO), expected)
            self.assertEqual(spell(value.upper(), NATO), expected)

            self.assertEqual(''.join(spell(value, string.ascii_lowercase)),
                             value.lower())
            self.assertEqual(''.join(spell(value, string.ascii_uppercase)),
                             value.upper())

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name', nargs='?', default='',
                        help='name to spell')
    args = parser.parse_args()

    if len(args.name) > 0:
        for word in spell(args.name):
            print('{} as in {}'.format(word[0].upper(), word))
    else:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(_UnitTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
