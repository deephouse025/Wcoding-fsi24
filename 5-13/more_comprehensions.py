# Generate your own lists of numbers, sentences, and strings for these
#  exercises and use several permutations to verify that they work
#  as intended!
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list_2 = [125, 100, 50, -50]
list_3 = [432, 2345, 323, 1, 6, 43, 33]
list_4 = "His dog barks loudly, my school starts at 8:00, they take the bus to work."
list_5 = ["apple", "mango", "banana", "strawberry", "lemon"]
word = "flatdisk"

# 1. Given a list of numbers, write a list comprehension that produces a
#     list of strings of each number that is divisible by 5.
([x for x in list_1 if x % 5 == 0])

# 2. Given a sentence, produce a list of the lengths of each word in the
#     sentence, but only if the word is not 'the'.
[len(wrd) for wrd in list_4.lower().split() if wrd != "the"]

# 3. Given a string representing a word, write a list comprehension that
#     produces a list of all the vowels in that word.
[ltr for ltr in "cubecone" if ltr in "aeiou" or "AEIOU"]

# 4. Given a string representing a word, write a set comprehension that
#     produces a set of all the vowels in that word.
{ltr for ltr in "flatdisk" if ltr in "aeiou" or "AEIOU"}

# 5. Given a sentence, return the sentence with all vowels removed.
no_vowels = [ltr for ltr in list_4 if ltr not in "aeiou" or "AEIOU"]
"".join(no_vowels)

# 6. Given a list of numbers, return the list with all even numbers doubled,
#     and all odd numbers turned negative.
print([_int*2 if _int%2==0 else _int*-1 for _int in list_1])

# 7. Given a sentence, return a new sentence with all its letters transposed
#     by 1 letter right in the alphabet, but only if the new letter is
#     between b and y, inclusive.
sentence = "Carry out a something something something with no exception of something else! woah!"
alphas = "abcdefghijklmnopqrstuvwxy"
print("".join([alphas[alphas.find(letter) + 1] if letter in alphas else letter for letter in sentence.lower()]))


# 8. Given a list of floats and ints, remove the floats (numbers with decimals).
