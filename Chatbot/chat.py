# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random

import json
import pickle

from Chatbot.Training import bow, classify, response, getResponse

base_path = 'Chatbot/'

data = pickle.load( open(base_path + "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import our chat-bot intents file
with open(base_path + 'intents.json') as json_data:
    intents = json.load(json_data)

# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# load our saved model
model.load('./' + base_path + 'model.tflearn')

def respond(sentence):
    return getResponse(sentence, model, words, classes, intents)

if __name__ == '__main__':
    while True:
        sentence = input("you: ")
        response(sentence, model, words, classes, intents)
        if sentence == str("Bye") or sentence == str("Goodbye"):
            break