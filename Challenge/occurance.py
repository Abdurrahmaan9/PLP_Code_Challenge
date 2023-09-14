from collections import Counter

def count_words(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the contents of the file and convert to lowercase
        text = file.read().lower()

        # Split the text into words
        words = text.split()

        # Count the occurrences of each word
        word_counts = Counter(words)

        # Get the top 10 most frequent words
        top_words = word_counts.most_common(10)

        return top_words

if __name__ == '__main__':
    # Specify the filename of the text file to process
    filename = 'example.txt'

    # Count the words and get the top words
    top_words = count_words(filename)

    # Print the top words with their counts
    print("Top 10 Most Frequent Words:")
    for word, count in top_words:
        print(f"{word}: {count}")
