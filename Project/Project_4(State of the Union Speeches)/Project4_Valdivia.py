# Author: Jose A. Valdivia Rojas
# Course: CMSC 206
# Project 4 - Final Submission
import re
import readability

### Main Functions
def process_file(file : str):
    with open(file) as f:
        text = f.read()
    results = readability.getmeasures(text, lang='en')
    print('Readibility Score:' , results['readability grades']['FleschReadingEase'])
    print()


# Function to get a list of words
def process_words(file : str):
    with open(file) as f:      # Open the file
        text = f.read()                # Read the file
        text = text.lower()           # Convert the whole text to lower case
        text = re.sub(u"[-()\"#$/@;:<>{}`+=~|!?,\â€“”\*]|\[.*\]|\d{1,}th|\d{1,}s|\d{1,}'s|\d{1,}", " ", text)
        list_words = re.split('[-\s—]', text)  # Split string with multiple delimiters: - , \s, — 

    list_words = [ (eachWord.strip('.,“”!;()-[]?,):\n"')) for eachWord in list_words]     # Cleaning the words from . , ! ; () [] “ ” ? ' 
    list_words = [ (eachWord.replace("’s" , '')) for eachWord in list_words]    # Replace 's from words with ''
    list_words = [ (eachWord.replace("’ll" , '')) for eachWord in list_words]    # Replace 'll from words ''
    list_words = [ (eachWord.replace("’t" , '')) for eachWord in list_words]    # Replace 't from words ''
    list_words = [ (eachWord.replace("'s" , '')) for eachWord in list_words]    # Replace 's from words with ''
    list_words = [ (eachWord.replace("'ll" , '')) for eachWord in list_words]    # Replace 'll from words ''
    list_words = [ (eachWord.replace("'t" , '')) for eachWord in list_words]    # Replace 't from words ''
    list_words = list(filter(None, list_words))         # Filter Null values or empty strings from the List  
    return list_words
    

# Function to get a list of sentences
def process_sentences(file : str):
    with open(file) as f:
        text = f.read()
        list_sentences = re.split('[?.:]', text)
    # Format the text in sentences
    list_sentences = [ (eachSentence.replace("\n" , '')) for eachSentence in list_sentences]    # Replace \n from sentence with '' to clean up
    list_sentences = [ (eachSentence.strip()) for eachSentence in list_sentences]               # Remove leading and trailing spaces
    list_sentences = [ (None if len(eachSentence) < 3 else eachSentence) for eachSentence in list_sentences ]   # If a sentence has less than 3 words so its not a sentence (Null)
    list_sentences = list(filter(None, list_sentences))         # Filter Null values from the List             
    return list_sentences

# Function to get the average number of words   
def avg_word(list_words : list):
    num_letters = int()
    num_words = len(list_words)
    for eachWord in list_words:
        num_letters += len(eachWord)
    return num_letters/num_words

# Function to get the average number of sentences
def avg_sentence(list_sentences : str):
    num_words = int()
    num_sentences = len(list_sentences)
    for eachSentence in list_sentences:
        word_per_sentence = eachSentence.split(' ')
        num_words += len(word_per_sentence)
    return num_words/num_sentences 

# Function that display the number of words and its average words
def wordCount(file : str):
    list_words = process_words(file)
    num_words = len(list_words)
    average_words = avg_word(list_words)
    print(f"\nThere are a total of {num_words} words with about {average_words} letters per word in {file}.")

# Function that display the number of sentences and its average sentences
def sentenceCount(file : str):
    list_sentences = process_sentences(file)
    num_sentences = len(list_sentences)
    average_sentences = avg_sentence(list_sentences)
    print(f"There are a total of {num_sentences} sentences with about {average_sentences} words per sentence in {file}.")

# Function that display the number of characters
def characterCount(file : str):
    num_character = int()
    list_words = process_words(file)
    for eachWord in list_words:
        num_character += len(eachWord)
    print(f"There are a total of {num_character} characters in {file}.")



def freq_words(file : str):
    from collections import Counter
    list_words = process_words(file)

    # Filter out values: the, a, an
    unwanted = ('the','a','an','to','and','of','we','that','in','our','is','it','for','i','or','do','this','on','who','not','but','us','as','are','their','so','be','if','by')
    list_words = [ words for words in list_words if words not in unwanted]

    # Counter module to count freq words        
    Counter = Counter(list_words)
    most_occur = Counter.most_common(15)

    # Print output and save freq words
    print(f"\nThe 15 most frequently used words in {file}")
    for (word,repetition) in most_occur:
        print("{:>10} : {:>5}".format(word, repetition))

def longest_words(file : str):
    list_words = process_words(file)

    print(f"\n\nThe 10 longest words in {file}")
    for i in range(10):
        longest = max(list_words, key=len)
        print(f"{longest}:   \t{len(longest)} characters")
        while longest in list_words:
            list_words.remove(longest)


# Define a function to plot word cloud
def plot_cloud(wordcloud):
    import matplotlib.pyplot as plt
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off")

# Plot wordCloud
def wordCloud(file : str):
    # Import packages
    from wordcloud import WordCloud, STOPWORDS
    import numpy as np
    from PIL import Image

    # Get text
    with open(file) as f:
        text = f.read()

    # Import image to np.array
    if file == 'Obama.txt':
        mask = np.array(Image.open('obama.png'))
    elif file == 'Biden.txt':
        mask = np.array(Image.open('biden.png'))
    elif file == 'Trump.txt':
        mask = np.array(Image.open('trump.png'))
    elif file == 'Kennedy.txt':
        mask = np.array(Image.open('kennedy.png'))
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='Navy', colormap='autumn', collocations=False, stopwords = STOPWORDS, mask=mask).generate(text)
    print(f"\nThe word cloud of {file}:")
    plot_cloud(wordcloud)

# Display programmer info
def programInfo():
    print("\n\nThanks for using this Program")
    print("Author:", "Jose Valdivia Rojas")
    print("Course:", "CMSC 206")
    print("Assignment:", "Project 4B (State of the Union Speeches)")
    print("© 2022 JOSE VALDIVIA ALL RIGHTS RESERVED")
    exit()


# Variables
user_input = ''
files = list()



### Main Program
while user_input.lower() != 'done':
    user_input = input("\n\nEnter name of files on at a time. When ready to compile, enter 'done': ")

    if user_input.lower() != 'done':
        try:
            process_file(user_input)
            files.append(user_input)
        except FileNotFoundError:
            print("File not found, try again.")
    else:
        break
    
for speech in range(len(files)):
    longest_words((files[speech]))
    freq_words((files[speech]))
    wordCount((files[speech]))
    sentenceCount((files[speech]))
    characterCount((files[speech]))
    wordCloud((files[speech]))

programInfo()

