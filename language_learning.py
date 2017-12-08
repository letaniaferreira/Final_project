import ast
import random

def keep_playing_game(play_game):
    """evaluates if user wants to play"""
   
    if play_game.lower() == "yes" or play_game.lower() == "y" or play_game.lower() == "yep":
        return True
    elif play_game.lower() == "no" or play_game.lower() == "n" or play_game == "5":
        print "Goodbye!"
        return False
    else:
        print "Invalid input"
        return False

def choice_of_topic():
    """allows user to choose a semantic category for game"""

    print "We can go over many things today: "
    print "\n"
    list_of_topics = ["1-Small talk", "2-Hotel", "3-Airport", "4-Restaurant", "5-Exit"]
    for each_topic in list_of_topics:
        print each_topic 
    print "\n"
    topic = raw_input("Please choose a number above to have some fun with that topic: ")
    print "\n"

    return topic

def valid_vocab_options(topic):
    """renders valid options of vocab options"""

    vocabulary_file = None

    if topic == "1":
        vocabulary_file = 'small_talk_vocab.py'
    elif topic == "2":
        vocabulary_file = 'hotel_vocab.py'
    elif topic == "3":
        vocabulary_file = 'airport_vocab.py'
    elif topic == "4":
        vocabulary_file = 'restaurant_vocab.py'

    return vocabulary_file

def invalid_vocab_options(topic):
    """renders invalid vocab options"""

    if topic == "5":
        print "Are you sure you want to exit?"
        quit = raw_input("Enter 1 for yes and 2 for no.")
    if quit == "1": 
        keep_playing_game("no")
        vocabulary_file = None  # when keep_playing_game is called it goes to 133 and crashs
    else:
        vocabulary_file = None
        print "Invalid option. Please enter a number 1 - 5" 
        

def import_vocab_file(file):
    """imports files from different topics"""
    open_file = open(file) 

    dict_list = []

    for line in open_file:
        dict_list.append(line)

    open_file.close() 

    return dict_list

def string_to_dict(dict_line): 

    lst = ast.literal_eval(dict_line)

    return lst


def formulating_question(lst):
    """formulates question"""

    
    for k, v in lst.items():
        question = lst["question"]

    print "Please choose the best translation for the Portuguese word: %s" % (question)
    print "\n"
    for key, value in lst.items():
        if key != "question":
            print value
    print "\n"
    answer = raw_input("> ")
    print "\n"    

    return answer

def giving_feedback(lst, answer):
    """evaluates answer"""
        
    if answer == lst["right_answer"]:
        print "Well done! Let's go over the next item or press 5 to Exit"
    elif answer == '5':
        print "You asked to exit. Goodbye, hope to see you again soon!"
    else:
        print "Not quite, Try again! or press 5 to Exit"


def main():
    """Greets player, allows player to choose a topic, calls formulating_question, calls giving_feedback, gives option to play another round"""

    print "\n"
    print "Welcome to Language Learning" 
    print "\n"
    print "Let's test your Portuguese knowledge!"

    print "\n"
    play_game = raw_input("Do you want to play a round of guessing game?: ")
    print "\n"  

    new_game_round = keep_playing_game(play_game)

    index = random.randint(0, 10)

    while new_game_round: ## and index in range(len(list_of_dictionaries)):

        topic_choice = choice_of_topic()
        if topic_choice != None:
            vocabulary_option = valid_vocab_options(topic_choice)
            if vocabulary_option == None:
                invalid_vocab_options(topic_choice)
            else:
                vocab_file = import_vocab_file(vocabulary_option)
            dict_index = vocab_file[index]# index referent to each line at vocab files
            dict_loop = string_to_dict(dict_index)
            users_answer = formulating_question(dict_loop)
            giving_feedback(dict_loop, users_answer)
            index = index + 1


            play_game = raw_input("Do you want to play a new round of guessing game?: ")

            print "\n"

            new_game_round = keep_playing_game(play_game)

        else:
            topic_choice = choice_of_topic()

        


if __name__ == '__main__':
    main()
