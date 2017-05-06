import string
import random
random_number = random.randint(1,10) #generates random number to incript message
stretch_of_incription = random_number #defines number of extra characters that should be skept in reading
lenght_of_incription = str(random_number) #transforms number of characters in string
print stretch_of_incription
print lenght_of_incription  
def incription_generator(size = stretch_of_incription, characters = string.ascii_letters + string.digits):
    """generates extra characters that should be skept in reading"""
    return  ''.join(random.choice(characters) for _ in range(size))

message = incription_generator()
print message
