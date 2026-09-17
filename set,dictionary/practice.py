# ===================== DICTIONARY =====================
# store data in key value, mutable
# key will unique

student = {
    "name": "Hafsa",
    "class": 12,
    "city": "Dal bandala samahni"
}

# Accessing
print(student["name"])
print(student["city"])

# updating
student["city"] = "Bhimber"
print(student)

student["RollNo"] = "FA25-BAI-019"
print(student)

student.pop("city")
print(student)

# function
print(student.keys())
print(student.values())
print(student.items())
print(student.get("class"))

# update
student.update({"city": "Bhimber"})
print(student)


# ===================== SET =====================
# like list but no repetition, and { }
language = {"python", "Java", "python", "C++", "python"}
print(language)
print(type(language))

# empty set = set()
emptyset = set()
print(type(emptyset))

# Adding and remove element
nums = {1, 2, 3}
nums_2 = {3, 4, 5}

print(nums.add(4))
print(nums.remove(2))
print(nums.pop())

print(nums.union(nums_2))
print(nums.intersection(nums_2))

# list to set
language_list = ["python", "Java", "python"]
language = set(language_list)
print(type(language))


# ===================== DICTIONARY (more examples) =====================
# create dictionary of 3 marks
Marks = {}

Math = int(input("Enter math marks:"))
bio = int(input("Enter bio marks:"))
Eng = int(input("Enter Eng marks:"))

Marks.update({"Math": Math, "bio": bio, "Eng": Eng})
print(Marks)

Marks = {}
Marks["Math"] = 90
Marks["bio"] = 80
Marks["Eng"] = 82
print(Marks)

# duplicate keys fail silently (last value overwrites)
d = {
    1: "int",
    2: "float"
}  # duplicate keys not allowed - last one wins, no error

dic_2 = {}
dic_2[1] = "int"
dic_2[str(1.0)] = "float"
print(dic_2)