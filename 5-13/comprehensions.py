# 1. Find all of the numbers from 1–1000 that are divisible by 8.
[num for num in range(1000) if num % 8 == 0]

# 2. Find all of the numbers from 1–1000 that have a 6 in them.
[num for num in range(1000) if "6" in str(num)]

# 3. Use the following for the questions below:
string = "Practice Problems to Drill List Comprehension into Your Head."

#    b. Count the number of spaces in a string (use string above).
spaces = [letter for letter in string if letter == " "]
(len(spaces))


#    c. Remove all of the vowels in a string (use string above).
no_vowels = [letter for letter in string if letter not in "aeiou"]
(''.join(no_vowels))

#    d. Find all of the words in a string that are less than 5 letters
#        (use string above).
words = string.split()
less_than_5 = [wrd for wrd in words if len(wrd) < 5]
(less_than_5)

#    e. Use a dictionary comprehension to count the length of each word in
#        a sentence (use string above).
words_length = {wrd: len(wrd) for wrd in words}
(words_length)


# 4. Use the following for the questions below:
nums = [i for i in range(1,1001)]

#    b. Write a list comprehension that produces a list of each number
#        doubled. (use nums list above).
[i * 2 for i in nums]


#    c. Write a list comprehension that produces a list of the squares of
#        each number (use nums list above).
[]

#    d. Write a list comprehension that produces a list of only the even
#        numbers in that list (use nums list above).

#    e. Write a list comprehension that produces a list of only the odd
#        numbers in that list (use nums list above).

#    f. Write a list comprehension that produces a list of only the positive
#        numbers in that list (use nums list above).


# 5. Create a dictionary from the following list with same key:value pairs.
#     eg. {"key": "key"}.
lst = ["NY", "FL", "CA", "VT"]
print({key: key for key in lst})



# 6. Using dict comprehension, create a dictionary where each number in the
#     range is the key and each item divided by 100 is the value. Use a
#     range from 100 to 160 with steps of 10.
print({_num: _num/100 for _num in range(100, 161, 10)})


# 7. Using dict comprehension and a conditional argument, create a
#     dictionary from the following dictionary where only the key:value
#     pairs with value above 2000 are taken to the new dictionary.
stonks = { "NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700 }
{newStonks: V for newStonks, V in stonks.items() if V > 2000}