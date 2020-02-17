import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
        "I love my dog", 
        "I love my cat",

]   

tokenizer = Tokenizer(num_words = 100) # take top 100 words and encode it as values
tokenizer.fit_on_texts(sentences) # takes data and encodes it
word_index = tokenizer.word_index # dict where key is the word and value is token of the word
print(word_index)
