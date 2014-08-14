# create a meathod that takes a word and an array of words
# compare the word to every word in the array using is_anagram method

def canonical(word):
    return sorted(word.lower())


def is_anagram(word_1, word_2):
    return canonical(word_1) == canonical(word_2)

def anagrams_for(word, array):
    matches = []
    for x in array:
        if is_anagram(word, x):
            matches.append(x)
    print matches

dictionary = ['acres', 'cares', 'Cesar', 'races', 'smelt', 'melts', 'etlsm']

# If the input word happens to be in the dictionary, it should be in the the returned array, too.
# The list should also be case-insensitive.
anagrams_for('acres', dictionary)   # => ['acres', 'cares', 'Cesar', 'races']
anagrams_for('ACRES', dictionary)   # => ['acres', 'cares', 'Cesar', 'races']
anagrams_for('Cesar', dictionary)   # => ['acres', 'cares', 'Cesar', 'races']

# Although "sacre" is not *in* the dictionary, several words in the dictionary are anagrams of "sacre"
anagrams_for('sacre', dictionary)   # => ['acres', 'cares', 'Cesar', 'races']

# Neither the input word nor the words in the dictionary need to be valid English words
anagrams_for('etlsm', dictionary)   # => ['smelt', 'melts', 'etlsm']

anagrams_for('unicorn', dictionary) # => []
