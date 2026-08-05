students = []

for i in range(3):
    name = input("Name: ")
    score = float(input("Score: "))

    students.append({
        "name": name,
        "score": score
    })


def check_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


for student in students:
    result = check_score(student["score"])

    print("--------------------")
    print("Name:", student["name"])
    print("Score:", student["score"])
    print("Result:", result)




