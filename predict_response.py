# Bibliotecas de pré-processamento de dados de texto
import nltk

import json
import pickle
import numpy as np
import random

ignore_words = ['?', '!',',','.', "'s", "'m"]

# Biblioteca load_model
import tensorflow
from data_preprocessing import get_stem_words

model = tensorflow.keras.models.load_model('./chatbot_model.h5')

# Carregue os arquivos de dados
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))


def preprocess_user_input(user_input):

    input_word_token_1 = nltk.word_tokenize(user_input)
    input_word_token_2 = get_stem_words(input_word_token_1, ignore_words) 
    input_word_token_2 = sorted(list(set(input_word_token_2)))

    bag=[]
    bag_of_words = []
   
    # Codificação dos dados de entrada 
    for word in words:            
        if word in input_word_token_2:              
            bag_of_words.append(1)
        else:
            bag_of_words.append(0) 
    bag.append(bag_of_words)
  
    return np.array(bag)

def bot_class_prediction(user_input):

    inp = preprocess_user_input(user_input)
    #3-uma vez que temos o saco de palavras, como definimos a classe?
    


def bot_response(user_input):

   predicted_class_label =  bot_class_prediction(user_input)
   predicted_class = classes[predicted_class_label]

   #2-para cada pergunta dentro da classe, qual resposta o bot pode dar?

   

print("Oi, eu sou a Estela, como posso ajudar?")

while True:
    print("pergunta do usuário e resposta do bot")
    #1-perguntas:
    

