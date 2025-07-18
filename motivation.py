import random

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Push yourself, because no one else is going to do it for you.",
    "Don’t watch the clock; do what it does. Keep going.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Small steps every day lead to big results."
]

def get_motivational_quote():
    return random.choice(quotes)