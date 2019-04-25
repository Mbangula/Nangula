import torch

from Training import evaluate

use_cuda = torch.cuda.is_available()

#load data
SOS_token = 0
EOS_token = 1
prints = False

def translate(input_sentence):
    encoder1 = torch.load('encoder')
    attn_decoder1 = torch.load('decoder')

    output_words, attentions = evaluate(
        encoder1, attn_decoder1, input_sentence)

    output = ' '.join(output_words)
    return output