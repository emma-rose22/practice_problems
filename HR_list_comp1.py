def list_comp(nums, limit):
    #take in three numbers that represent coordinates 
    # another number is passed in as a limit
    # the goal is to print all possible coordinates of the input
    # where the sum of these are not equal to the limit

    #while sum(output) != limit:

    # print as many dimensions as necessary
    # print([nums for (i + 1) in range(x) for ])
    pass

def every_cube(x, y, z, limit):
    #have a master array
    array = []

    #moves through the array
    tracker = 0

    #go through every possibility of the coordinates
    for i in range(x + 1):
        for j in range(y + 1):
            for n in range(z + 1):
                if i + j + n != limit:
                    #add a new list in the list
                    array.append([])

                    #set that equal to the tracker
                    array[tracker] = [i, j, n]
                    
                    #move tracker to the next section of the array
                    tracker += 1

    print(sorted(array))
every_cube(1, 1, 1, 2)

def better_every_cube(x, y, z, limit):
    '''does not work'''
    #print[[i, j, n] for i in range(x+1) for j in range(y+1) for n in range(z+1) if sum([i,j,n]) != limit]
    print((x + 1 for i in range(x)) and (y + 1 for j in range(y)) and (z + 1 for n in range(x)))

print()
better_every_cube(1, 1, 1, 2)