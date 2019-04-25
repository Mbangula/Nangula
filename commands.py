t_commands = ["Translate", "translate", "Please translate", "please translate"]
s_commands = ["Search", "search", "Please search", "please search", "Search something for me", "search something for me","konga","Konga"]
q_commands = ["Quit", "quit", "Bye", "bye", "Goodbye", "goodbye","exit","Exit","oshili nawa","Oshili nawa"]

def tc(user_input):
    inlist = False
    if user_input in t_commands:
        inlist = True
    return inlist
def ts(user_input):
    inlist = False
    if user_input in s_commands:
        inlist = True
    return inlist
def tq(user_input):
    inlist = False
    if user_input in q_commands:
        inlist = True
    return inlist