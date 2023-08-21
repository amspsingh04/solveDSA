import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from textblob import TextBlob

# Load the default English stop words
stopwords = stopwords.words('english')

# Create a PorterStemmer object
stemmer = PorterStemmer()

# Get the input string
input_string = "This is a sentance with some speling errors."

# Tokenize the input string
tokens = nltk.word_tokenize(input_string)

# Remove all stop words
filtered_tokens = [token for token in tokens if token not in stopwords]

# Stem the filtered tokens
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

# Check for words that may have spelling mistakes
misspelled_words = []
for token in stemmed_tokens:
    if token not in nltk.corpus.words.words():
        misspelled_words.append(token)

# Correct the misspelled words
corrected_words = []
for misspelled_word in misspelled_words:
    corrected_word = TextBlob(misspelled_word).correct()
    corrected_words.append(corrected_word)

# Create a list of words from the word sheet
wordlist = []
with open("wordlist.txt", "r") as f:
    for line in f:
        wordlist.append(line.strip())

# Compare the corrected words and the left over words with the wordlist
matching_words = []
for word in filtered_tokens + corrected_words:
    if word in wordlist:
        matching_words.append(word)

# Print the matching words
print(matching_words)
