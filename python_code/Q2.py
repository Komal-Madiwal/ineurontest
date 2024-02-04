def highest_frequency_word(s):
    word_counts = {}
    words = s.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    if not word_counts:
        return 0

    max_word = max(word_counts, key=word_counts.get)
    return len(max_word)





print("Two test cases")

print("--------------------------------------------------------------------------------------")

input_string1 = "apple orange strawberry  banana apple orange strawberry  banana strawberry  apple strawberry "
output_1 = highest_frequency_word(input_string1)
print(f"Max word length of input_string1 is {output_1}")  ##output - 10


print("--------------------------------------------------------------------------------------")

# Example usage for input_string3
input_string3 = "hello world hello world world world"
output_3 = highest_frequency_word(input_string3)
print(f"Max word length of input_string3 is {output_3}")  #output 5

