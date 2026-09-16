# take a string and checks a particular word.
str = "I'm doing programming in c++"
print("python" in str)
result = {True: "present", False: "Not present"}
print(f"python {result[("python" in str)]} in sentence.")