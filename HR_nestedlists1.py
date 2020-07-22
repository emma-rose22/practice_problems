'''Given the names and grades for each student in a Physics class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.'''


# if __name__ == '__main__':
#     all_students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         all_students.append([name, score])

def second_lowest(all_students):
    #sort the lists by their second value
    all_students.sort(key=lambda x: x[1])

    #create a list of all those with second place scores
    second = []
    #create a list with only the scores
    only_scores = []

    #add all the scores to a list
    for i in all_students:
        only_scores.append(i[-1])

    #turn them into a set and sort them
    only_scores = list(set(only_scores))
    only_scores.sort()

    #search for any students with the second lowest score
    for i in all_students:
        if i[-1] == only_scores[1]:
            second.append(i)
    
    #sort the students with second lowest by name, and print name
    second = sorted(second)
    for i in second:
        print(i[0])

#second_lowest([['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]])

second_lowest([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]])