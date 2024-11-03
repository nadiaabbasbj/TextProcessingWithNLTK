Text Processing and Tokenization with NLTK
This project demonstrates text tokenization and preprocessing using Python's Natural Language Toolkit (NLTK). The steps cover tokenizing text into individual words and performing additional preprocessing like lowercasing, stopword removal, special character removal, and lemmatization. These techniques are fundamental in preparing text data for NLP (Natural Language Processing) tasks.

Table of Contents

Requirements

Setup

Usage

Explanation of Steps

Sample Output

Requirements
Python 3.6 or higher
NLTK library

Setup
To run this project, follow these setup instructions:

Install the NLTK library:
pip install nltk

Download the necessary NLTK data packages:
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

Usage
Clone this repository or download the TextProcessing.py file to your local machine.
Open a terminal and navigate to the project directory:
cd path/to/your/project

Run the script:
python TextProcessing.py

Explanation of Steps
The script processes a sample text paragraph by performing the following steps:

Tokenization: Breaks down the text into individual words or "tokens."
Token Count: Counts the total number of tokens.
Frequency Distribution: Displays the frequency of each token using nltk.FreqDist.
Lowercasing: Converts all tokens to lowercase to ensure uniformity.
Stopword Removal: Removes common English stopwords like "is," "and," which don’t contribute significant meaning.
Special Character Removal: Cleans the text by removing punctuation and special characters.
Lemmatization: Reduces words to their base forms (e.g., "running" to "run"), making text analysis more effective.
Each step's output is printed in the terminal to visualize the text transformations.

Sample Output
Here is a sample output after processing a sample paragraph:

Tokens
['Natural', 'Language', 'Processing', '(', 'NLP', ')', 'is', 'a', 'fascinating', ...]

Number of Tokens
54

Frequency Distribution of Tokens
FreqDist({'language': 2, 'NLP': 2, 'and': 2, 'in': 2, ...})

After Lowercasing
natural language processing (nlp) is a fascinating field ...

After Stopword Removal
['Natural', 'Language', 'Processing', 'NLP', 'fascinating', 'field', ...]

After Special Character Removal
natural language processing nlp is a fascinating field ...

After Lemmatization
['Natural', 'Language', 'Processing', 'NLP', 'fascinating', 'field', 'combine', ...]
