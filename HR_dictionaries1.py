'''
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, 
Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names
and marks for N students. You are required to save the record in a dictionary data type. The user then enters 
a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
'''

def student_average(dictionary, student):
    #search the dictionary for the student
    student_scores = dictionary[student]
    #average the numbers of their scores
    average = round(sum(student_scores) / len(student_scores), 2)
    #round and return the average
    print("{0:.2f}".format(average))



student_average({'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}, 'Malika')