'''
Given two strings, determine if they share a common substring. A 
substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . 
The words "be" and "cat" do not share a substring.
'''

#this has the best runtime out of initial coding varieties

def twoStrings(s1, s2):
    s1 = list(set(s1))
    cache = {}
    for i in s1:
        cache[i] = 1

    for i in s2:
        if i in cache.keys():
            return 'YES'
        else:
            pass
    return 'NO'