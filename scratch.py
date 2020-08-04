import random

tried = []
def findSecretWord(wordlist):
    global tried
    if len(tried) == 0:
        guess = random.choice(wordlist)
        tried.append(guess)
        return guess
    else:
        run = True
        while run:
            guess = random.choice(wordlist)
            if guess not in tried:
                tried.append(guess)
                run = False
                return guess


target = "acckzz"
words = ["acckzz","ccbazz","eiowzz","abcczz"]

run = True
counter = 0
while run:
    result = findSecretWord(words)
    counter += 1
    if result == target:
        run = False
print(counter)