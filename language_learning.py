print "Welcome to Language Learning" 
print "We can go over many things today: "
topics = ["-Greetings", "-Hotel", "-Airport", "-Restaurant", "-Exit"]
for variable in topics:
    print variable 
start = raw_input("Please choose a topic above to learn more about it: ")
if start.strip().lower() == "greetings":
    print "Lets play a guessing game."
    print " Please choose the best translation for each of the items bellow: "
    greetings = ["oi", "tudo bem?", "como vai?", "qual o seu nome?", "tchau", "bom dia" "boa tarde", "boa noite"]
    for item in greetings:
        print item


