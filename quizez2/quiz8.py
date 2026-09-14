# Take two students' test scores as input and determine, using only logical operators (no if-else), whether both passed given a passing score of 40
score_1 = float(input("Enter student 1 marks:"))
score_2 = float(input("Enter student 2 marks:"))

Passing_marks = 40

result = {True: "Pass", False: "Fail"}

print(result[score_1 >= Passing_marks])
print(result[score_2 >= Passing_marks])