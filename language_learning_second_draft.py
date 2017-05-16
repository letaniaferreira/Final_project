print "\n"
print "Welcome to Language Learning" 
print "\n"
print "Let's test your Portuguese knowledge!"
print "\n"
print "We can go over many things today: "
topics = ["1-Small talk", "2-Hotel", "3-Airport", "4-Restaurant", "5-Exit"]
for variable in topics:
    print variable 
start = raw_input("Please choose a number above to have some fun with that topic: ")
if start == "1":
    print "Lets play a guessing game."
    print " Please choose the best translation for each of the items bellow: "
    #time = ["bom dia", "boa tarde", "boa noite"]
    #for item in greetings:
        #print item
    #hi = ["oi", "tudo bem?", "como vai?", "qual o seu nome?"]
    print "\n"
    
    question = "tchau"
    lst = { "Q": "tchau", "IA1":'hello', "RA":'goodbye', "IA2":'you are welcome'}

    def formulating_question(question):
        """formulates question"""


        print "For the Portuguese word: %s" % (question)
        print "\n"
        print "What is the best English translation?"
        print "\n"
        
        for key, value in lst.items():
            if key != "Q":
                print value
    formulating_question(question)

    print "\n"


    answer = raw_input('>')
    print "\n"

    def giving_feedback(answer):
        """evaluates answer"""
        
        if answer == lst["RA"]:
            print "Well done! Let's go over the next item or press 5 to Exit"
        elif answer == '5':
            print "You asked to exit. Goodbye, hope to see you again soon!"
        else:
            print "Not quite, Try again! or press 5 to Exit"

    giving_feedback(answer)    



