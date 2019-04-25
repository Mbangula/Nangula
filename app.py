from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
import sys
import traceback
import logging
import googleSearch as gs
import Chatbot.chat as chat
import Translate as tr
import commands as cmd

# Use of translate function needs these imports
from Training import EncoderRNN
from Training import AttnDecoderRNN

state = {
    'debug': False,
    'translate': False,
    'search': False
}

input_style = Style.from_dict({
    '': '#33aa33 bold',
})

def exit():
    print("See you later alligator!")
    sys.exit()

def getTranslation(user_input, state):
    try:
        translate = tr.translate(user_input);
    except KeyError:
        if state['debug']:
            logging.error(traceback.format_exc())
        else:
            translate = "Ouh, man. I don't know that word"
    return translate
def getSearch(user_input, state):
	search = gs.search(user_input);
	return search
def getOutput(user_input, state):
    if user_input == "debug":
        state['debug'] = True
        return "I let you know what is inside me"
    if user_input == "stop debug":
        state['debug'] = False
        return "I will keep my poker face from now on"
    if cmd.tq(user_input):
       print(user_input)
       exit()
    if cmd.tc(user_input):
        print("moi")
        state['translate'] = True
        return "Sure, I will translate from Oshiwambo to English"
    if user_input == "stop translating":
        state['translate'] = False
        return "Okay, let's talk about something"
    if cmd.ts(user_input):
	    state['search']  = True
	    return "What do you want to search about"
    if user_input == "stop searching":
	    state['search'] = False
	    return "Okay, is there anything else"

    if state['search']:
	    return getSearch(user_input, state)
    if state['translate']:
        return getTranslation(user_input, state)
    else:
        return chat.respond(user_input)


if __name__ == '__main__':
    print('')
    file = open('polar-bear.txt', 'r')
    print(file.read())
    print('')
    print('Welcome to meet Jääkarhu (polar bear), a chat bot')
    print('')

    while True:
        try:
            answer = prompt('You: ', style=input_style)
            print('Bot: %s' % getOutput(answer, state))
        except EOFError:
            pass
        except KeyboardInterrupt:
            exit()
        except Exception: # catch *all* exceptions
            if state['debug']:
                logging.error(traceback.format_exc())
