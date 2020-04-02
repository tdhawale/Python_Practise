import nltk
import numpy as np
import random
import string
import warnings

from sklearn.feature_extraction.text import TfidfVectorizer

# use cosine similarity concept to generate a response from the bot by comparing the similarity between user input and the data present in the corpus
from sklearn.metrics.pairwise import cosine_similarity

# Use wikipedia QnA data as corpus
filename = "WikiQnA.txt"

f = open(filename , 'r' , errors = 'ignore')
raw_text = f.read()

raw_text = raw_text.lower()

nltk.download('punkt')

# WordNet is a semantically-oriented dictionary of English included in NLTK.
nltk.download('wordnet')

# convert to list of sentences
sentence_tokens = nltk.sent_tokenize(raw_text)
# print(type((sentence_tokens)))
# print(len((sentence_tokens)))
# print(sentence_tokens[:5])

# convert to list of words
word_tokens = nltk.word_tokenize(raw_text)
# print(type((word_tokens)))
# print(len(word_tokens))
# print(word_tokens[:5])

# We shall now define a function called LemTokens which will take as input the tokens and return normalized tokens.
lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens) :
	return [lemmer.lemmatize(token) for token in tokens]


remove_punctuation_dict = dict((ord(punct) , None) for punct in string.punctuation)


def LemNormalize(text) :
	return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_dict)))


# The bot should return a greeting if the user input is a greeting
greeting_input = ["hi" , "hello" , "what's up" , "hola" , "hey" , "how are you"]

greeting_response = ["hi" , "hello" , "what's up" , "hola" , "hey" , "hi there"]


def greeting(sentence) :
	for word in sentence.split() :
		if word.lower() in greeting_input :
			return random.choice(greeting_response)


# The user enters an utterance and the bot tries to return an appropriate response using known information from the corpus, else it says "Sorry, I didn't understand that"
def response(user_input) :
	bot_response = ""
	sentence_tokens.append(user_input)
	#     print(sentence_tokens)
	
	TfidVect = TfidfVectorizer(tokenizer = LemNormalize , stop_words = 'english')
	TfidFit = TfidVect.fit_transform(sentence_tokens)
	
	vals = cosine_similarity(TfidFit[-1] , TfidFit)
	idx = vals.argsort()[0][-2]
	
	flat = vals.flatten()
	flat.sort()
	req_TfidFit = flat[-2]
	
	if req_TfidFit == 0 :
		bot_response = bot_response + "Sorry, I didn't understand!\n"
		return bot_response
	else :
		bot_response = bot_response + sentence_tokens[idx]
		return bot_response
	

# Some minor tweaks regarding what the bot should say while starting and ending the convo
flag = True
print("BOT: \nMy name is BOT. Chat-BOT (*suspense music in the background*). \nI will tell you about some common FAQs about various topics. \nIf you wish to quit, simply type bye!\n\n")

while flag==True:
    user_input = input()
    user_input = user_input.lower()
    if user_input not in ["bye", "quit", "exit"]:
        if user_input in ["thanks", "thank you", "danke"]:
            flag = False
            print("\nBOT: You are very much welcome!")
        else:
            if greeting(user_input) != None:
                print("\nBOT: \n" + greeting(user_input))
            else:
                print("\nBOT: Here is a popular FAQ related to your query\n", response(user_input) + "\n")
                sentence_tokens.remove(user_input)
    else:
        flag = False
        print("Bot: Bye! See you soon.\n")
