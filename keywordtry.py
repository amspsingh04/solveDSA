import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tag import postag

nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text):
    # Tokenization
    tokens = word_tokenize(text)
    
    # Lowercase and remove stopwords
    tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stopwords.words('english')]
    
    # Part-of-Speech tagging
    tagged_tokens = pos_tag(tokens)
    
    # Extract nouns and adjectives
    keywords = [word for word, pos in tagged_tokens if pos in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS']]
    
    # Frequency analysis
    fdist = FreqDist(keywords)
    
    # Rank keywords based on frequency
    ranked_keywords = sorted(fdist.items(), key=lambda item: item[1], reverse=True)
    
    # Return top keywords
    return [word for word, freq in ranked_keywords[:5]]  # Return top 5 keywords

text = "How to sort an array in Python using quicksort algorithm?"
keywords = extract_keywords(text)
print(keywords)
