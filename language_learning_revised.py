from dict_file import *
import ast

def guessing_game(user_choice):
    """takes yes or no and evaluates if user wants to play"""
    if user_choice.lower() == "yes" or user_choice.lower() == "y":
        return True
    if user_choice.lower() == "no" or user_choice.lower() == "n":
        return False



def import_list(file):
    """imports files from different topics"""
    open_file = open(file)

    dict_list = []

    for line in open_file:
        dict_list.append(line)

    open_file.close() ### is this in the correct place?

    return dict_list

def looping_through_dict(lista):

    dict_line = lista[0] 
    lst = ast.literal_eval(dict_line)

    return lst


def formulating_question(lst):
    """formulates question"""

    
    for k, v in lst.items():
        question = lst["Q"]

    print "Please choose the best translation for the Portuguese word: %s" % (question)
    print "\n"
    for key, value in lst.items():
        if key != "Q":
            print value
    print "\n"
    answer = raw_input("> ")
    print "\n"    

    return answer

def giving_feedback(lst, answer):
    """evaluates answer"""
        
    if answer == lst["RA"]:
        print "Well done! Let's go over the next item or press 5 to Exit"
    elif answer == '5':
        print "You asked to exit. Goodbye, hope to see you again soon!"
    else:
        print "Not quite, Try again! or press 5 to Exit"


def main():
    """Greets player, allows player to choose a topic, calls formulating_question, calls giving_feedback, gives option to play another round"""
    
    import_list('dict_file.py')

    print "\n"
    print "Welcome to Language Learning" 
    print "\n"
    print "Let's test your Portuguese knowledge!"
    print "\n"
    print "We can go over many things today: "
    print "\n"
    topics = ["1-Small talk", "2-Hotel", "3-Airport", "4-Restaurant", "5-Exit"]
    for topic in topics:
        print topic 
    start = raw_input("Please choose a number above to have some fun with that topic: ")
    print "\n"
    if start == "1":
    

        #print " Please choose the best translation for each of the items bellow: "
    #time = ["bom dia", "boa tarde", "boa noite"]
    #for item in greetings:
        #print item
    #hi = ["oi", "tudo bem?", "como vai?", "qual o seu nome?"]
        print "\n"


        user_choice = raw_input("Do you want to play a round of guessing game?: ")

        print "\n"

    new_game_round = guessing_game(user_choice)

    while new_game_round:

        list_of_dictionaries = import_list('dict_file.py')
        dict_loop = looping_through_dict(list_of_dictionaries)
        users_answer = formulating_question(dict_loop)
        giving_feedback(dict_loop, users_answer)


        user_choice = raw_input("Do you want to play a new round of guessing game?: ")

        print "\n"

        new_game_round = guessing_game(user_choice)

        


if __name__ == '__main__':
    main()
