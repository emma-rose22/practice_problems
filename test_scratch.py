'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.

There are no characters in this string that do not repeat.
'''

def first_not_repeating_character(s):
    #put each letter as a key in dict, value is times sighted 
    #get the keys that were sighted once
    #  if none return _
    #get their index position in the OG string, and return the letter
    #at the first index position
    cache = {}
    repeats = []
    index_pos = []
    
    #inserting all into cache
    for letter in s:
        if letter in cache:
            cache[letter] += 1
        else:
            cache[letter] = 1
            
    #getting all the values that appeared once
    for key in cache:
        if cache[key] == 1:
            repeats.append(key)
    #if repeats isn't empty
    #get all their index positions in OG list
    #and return the smallest one
    if len(repeats) > 0:
        for repeat in repeats:
            index = s.index(repeat)
            index_pos.append(index)
        smallest = min(index_pos)
        return s[smallest]
    else:
        return '_'
    
s = "abacabad"
#print(first_not_repeating_character(s))

'''
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Pers
'''

def uncover_spy(n, trust):
    #two lists
    # one with trusted people
    # one with possible spies
    # when we add trusted people to list (every 1st in pair)
    #  check if they are in possible spies
    #     if so, remove them
    # to see if we add someone to the spies list
    #    check if they are already trusted
    #       if so dont add to spies
    #       else add
    trusted = []
    maybe_spies = []
    
    for nest in trust:
        #put all the trusters in trusted
        trusted.append(nest[0])
        if nest[0] in maybe_spies:
            #if truster in spies, take them out
            maybe_spies = list(filter(lambda x: x != nest[0], maybe_spies))
        #if not trusted not in trusted list, add to spies
        if nest[1] not in trusted:
            maybe_spies.append(nest[1])
        
    #if there is just one spy left
    one_spies = list(set(maybe_spies))
    #and they are trusted by n - 1 people
    # (so they show up in the spies list n- 1 times)
    everyone_trusts = len(maybe_spies)
    #return them as the spy
    if (len(one_spies) == 1) and everyone_trusts == (n-1):
        return maybe_spies[0]
    else:
        return -1

n = 3
trust = [[1,2], 
        [2,3]]

#print(uncover_spy(n, trust))


'''
Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

For example, if we have the following linked list: 
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

After the function executes, the state of the linked list should be:
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

If k is longer than the length of the linked list, the linked list should not be changed.

Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?
'''

def remove_kth_from_end(head, k):
    #iterate through the list
    # by the k iteration, start pointer incrementing from the head
    # when we get to the end, pointer should be pointing at the given node
    
    counter = 0
    pointer = head
    before_k = None
    
    while pointer:
        counter += 1
        
        #if the counter is two past the node we want to delete
        #start the before k at the heaad
        if counter == k + 2:
            before_k = head
            
        #increment the position before the node we want to delete
        if before_k:
            before_k = before_k.next
        #increment pointer used to move through list
        pointer = pointer.next
        
    #cant start pointer if k == len(list)
    #but that means it is always the head that is deleted
    if counter == k:
        head = head.next
    try:
        before_k.next = before_k.next.next
    except:
        pass
        
    return head


head = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
k = 4

print(remove_kth_from_end(head, k))