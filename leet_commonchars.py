'''
Given an array A of strings made only from lowercase letters, return a list of all characters 
that show up in all strings within the list (including duplicates).  For example, if a character
 occurs 3 times in all strings but not 4 times, you need to include that character three times 
 in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
'''

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        #make a dictionary for each word that counts the letters
        #add all letters to a set
        #use set to search through dicts
            #if letter in all and count is same in all,
            #print letter that many times
            #if letter and all but count is different, print lowest count
            #else print nothing
        storage = list()
        word_count = []
        answer = []
        
        for word in A:
            split = set(word)
            count = Counter(word)
            word_count.append(count)
            storage.append(split)
        u = set.intersection(*storage)
        
        
        for letter in u:
            letter_count = []
            for cache in word_count:
                letter_count.append(cache[letter])
            answer += list(letter * min(letter_count))
            
        return answer
            