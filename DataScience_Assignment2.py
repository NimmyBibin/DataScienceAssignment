from collections import Counter
def is_valid_string(s):
    char_counts = Counter(s)
    #count the frequency of each character
    frequencies = list(char_counts.values())
    # Count the frequency occurrences
    freq_counts = Counter(frequencies)
    # if all the characters having same frequency, the string is valid
    if len(freq_counts )== 1:
        return "YES"
    # If there are more than two different frequencies, the string is not valid
    if len(freq_counts) > 2:
            return "NO"
    # If there are exactly two different frequencies
    freq1, count1 = freq_counts.most_common(1)[0]
    freq2, count2 = freq_counts.most_common(2)[1]
    # If removing one character can make all remaining characters have the same frequency
    if (count1 == 1 and freq1 == 1) or (count2 == 1 and freq2 == 1) or (count1 == 1 and freq1 - freq2 == 1) or (
            count2 == 1 and freq2 - freq1 == 1):
        return "YES"

    return "NO"
# Example1
input_string = "abc"
result = is_valid_string(input_string)
print(result)
# Example2
input_string = "aaabbcc"
result = is_valid_string(input_string)
print(result)
# Example3
input_string = "NimyYYyy"
result = is_valid_string(input_string)
print(result)
