import random
names = ["Steve", "Judy", "Peggy", "Anne", "Tom", "Paul", "Rose"]

# syntax new_dictionary = {new_key:newValue for item in anyIterable}

students_scores = {student:random.randint(1, 100) for student in names}

# loop through dictionary find 60 or more syntax
# new_dictionary = {new_key: new_value for (key, value) in dict.items()  if test }
passed_students ={student:score for (student, score) in students_scores.items() if score > 60}