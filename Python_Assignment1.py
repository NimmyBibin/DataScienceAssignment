def length_highest_frequency_word(input_string):
    word_frequency= {}
# Split the string into words
    words = input_string.split()
# Count the frequency of each word using for loop
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
# Find the highest frequency
    highest_frequency= max(word_frequency.values())
# Find the length of the highest-frequency word
    highest_freq_word = max(word_frequency, key=word_frequency.get)
    highest_freq_word_length = len(highest_freq_word)
    return highest_freq_word_length
#Example1
input_string = "welcome welcom home i am happy to invite you"
result = length_highest_frequency_word(input_string)
print("Length of the highest-frequency word:", result)
#output1:Length of the highest-frequency word: 7
"""Explanation - From the given string we can note that the most frequent word is “welcome” and
 the maximum value is 2 and its corresponding length is 7"""
#Example2
input_string = "I am very very happy and i would like like like to know more about datascience"
result = length_highest_frequency_word(input_string)
print("Length of the highest-frequency word:", result)
#output1:Length of the highest-frequency word: 4
"""Explanation - From the given string we can note that the most frequent words are “very” and “like” and
the maximum count is 2 and its corresponding max length is 4"""

#Example3
input_string = "welcome welcome home i am happy happy to invite you"
result = length_highest_frequency_word(input_string)
print("Length of the highest-frequency word:", result)
#output1:Length of the highest-frequency word: 7
"""Explanation - From the given string we can note that the most frequent word is “welcome” and "happy"
 the maximum count is 2 and its corresponding  max length is 7"""


