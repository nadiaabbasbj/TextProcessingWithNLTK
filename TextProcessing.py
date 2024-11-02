# Import necessary libraries
import nltk
import re
import spacy
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords


# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Step 2: Define a text variable with a sample paragraph
text = """Natural Language Processing (NLP) is a fascinating field that combines linguistics and artificial intelligence. 
It allows computers to understand, interpret, and respond to human language. With advancements in AI, NLP has evolved significantly. 
Techniques like tokenization help in breaking down complex language into manageable pieces."""

# Step 3: Tokenize the text into words
tokens = nltk.word_tokenize(text)
print("Tokens:", tokens)

# Step 4: Count the number of tokens
num_tokens = len(tokens)
print("Number of tokens:", num_tokens)

# Step 5: Calculate the frequency distribution of tokens
freq_dist = FreqDist(tokens)
print("Frequency Distribution of Tokens:", freq_dist)

# Step 6: Print tokens with their respective frequencies
for token, frequency in freq_dist.items():
    print(f"{token}: {frequency}")

# tried a few more TextProcessing steps:
# Lowercasing
text = text.lower()
print("After Lowercasing:", text)

# Stopword Removal
filtered_text = [word for word in tokens if word not in stopwords.words('english')]
print("After Stopword Removal:", filtered_text)

# Removing special characters
text = re.sub(r'[^a-zA-Z\s]', '', text)
print("After Removing Special Characters:", text)

# Lemmatization with Spacy
# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")
lemmatized_text = [token.lemma_ for token in nlp(" ".join(filtered_text))]
print("After Lemmatization:", lemmatized_text)