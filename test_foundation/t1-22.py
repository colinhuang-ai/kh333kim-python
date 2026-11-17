# Complete the following function to compute the frequency of each word length in a list of
# strings, returning the result as a dictionary. The order of keys in the returned dictionary does not
# matter.
# Example:
# Input: length_frequency(["cat", "dog", "elephant", "ant", "bear"])
# Output / Return: {3: 3, 8: 1, 4: 1}
def length_frequency(words):
    # Step 1: loop through the list of words and calculate the length of each word
    # if words = ["cat", "dog", "elephant", "ant", "bear"]
    word_lengths = [len(word) for word in words] # list [3,3,8,3,4]
    print(f"Word lengths: {word_lengths}")

    # Step 2: use a dictionary to keep track of the frequency of each word length
    # dict { "3": 0}, if next word_length = 3, count + 1
    frequency = {} # dict: key = length of word -> count = frequency of that length
    for length in word_lengths:
        frequency[length] = frequency.get(length, 0) + 1

    return frequency
# end function


# test1, test the function with a sample input
words = ["cat", "dog", "elephant", "ant", "bear"]
list_length_frequency = length_frequency(words)
print(f"Length frequency: {list_length_frequency}")

# test2, test the function with another sample input
words2 = ["hello", "world", "python", "is", "great"]
print(f"Length frequency: {length_frequency(words2)}")

# unittest for length_frequency function
# import unittest

# class TestLengthFrequency(unittest.TestCase):
#     def test_length_frequency(self):
#         # Test case 1
#         words = ["cat", "dog", "elephant", "ant", "bear"]
#         expected = {3: 3, 8: 1, 4: 1}
#         self.assertEqual(length_frequency(words), expected)

#         # Test case 2
#         words = ["hello", "world", "python", "are", "great"]
#         expected = {5: 3, 3: 1, 6: 1}
#         self.assertEqual(length_frequency(words), expected)

# if __name__ == '__main__':
#     unittest.main()
