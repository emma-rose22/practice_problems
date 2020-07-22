#take in length of list
# take in list of scores
# print second highest score


def print_runnerup(len, scores):
    scores = sorted(list(set(scores)))
    print(scores)
    print(scores[-2])

print_runnerup(5, [2, 3, 6, 6, 5])
print_runnerup(5, [2, 4, 3, 8, 7])
print_runnerup(4, [57, 57, -57, 57])