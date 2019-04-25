import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import json
import pickle

stemmer = LancasterStemmer()
#loading contents from the intents file

with open('intents.json') as intents_data:
	intents = json.load(json_data)

words = []
classes = []
documents = []
ignore_words = {'?'}

for intent in intents ['patterns']:
	for pattern in intent ['patterns']:
		w = nltk.word_tokenize(pattern)
		words.extend(w)
		documents.append((w, intent['tag']))
# create our training data
training = []
output = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

#model

tf.reset_default_graph()
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')


