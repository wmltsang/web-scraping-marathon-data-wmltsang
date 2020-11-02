from random import randint


def generate_sequence():
    for _ in range(randint(1, 10)):
        yield True
    
    while True:
        yield False
        

def generate_html():
    for _ in range(randint(1, 10)):
        yield "<p>This contains text!</p>"
    
    while True:
        yield "<p></p>"
