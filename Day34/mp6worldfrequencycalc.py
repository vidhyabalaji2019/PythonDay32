# Mini Project 6: Word Frequency Counter

# Ask the user for a sentence
sentence = input("Enter a sentence: ").lower()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the results
print("\nWord Frequency Count:")
for index, (word, count) in enumerate(word_count.items(), start=1):
    print(f"{index}. {word} -> {count}")
