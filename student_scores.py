students = []

for i in range(2):
    name=input("Name:")
    score=float(input("Score:"))
students.append({

    "name": name,
    "score":score
})    
def check_score(score):
    if score>=85 :
        return "excellent"
    elif score>=50 :
        return "pass"
    else :
        return "fail"

for student in students :

    result =check_score(student["score"])

    print("*****************************")
    print("Name:", student ["name"])
    print("Score:", student["score"])
    print("Result:", result)

highestscore=0
higheststudent=""

for student in students :
 if highestscore<student["score"] :
    highestscore=student["score"]
    higheststudent=student["name"]
    print("Highestscore:", highestscore)
    print("Higheststudent:",higheststudent)

