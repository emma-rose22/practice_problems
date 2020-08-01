'''
Given an integer, n, and  space-separated integers as input, create a tuple, t, of those n integers. 
Then compute and print the result of hash(t).
'''

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

def make_tuple(integer_list):
    l = list(integer_list)
    tup = ()
    for i in l:
        tup = tup + (i,)
    print(hash(tup))

make_tuple(integer_list)