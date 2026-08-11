
students = []

for i in range(3):
    name = input("Name: ")
    score= float(input("Score: "))

    students.append({
        "name": name,
        "Score": score
    })


def check_score(x):
    if x >= 90:
        return "Excellent"
    elif x >= 50:
        return "Pass"
    else:
        return "Fail"
    

for student in students:
    
    result = check_score(student["Score"])
    

    print("--------------------")
    print("Name:", student["name"])#HAVASET BA FASELE HA BASHE
    print("Score:", student["Score"])
    print("Result:", result)

highestscore=0
highestudent=""
total = 0 

for student in students:
    if highestscore<student["Score"] :
     highestscore = student["Score"] 
     highestudent = student["name"] 
     total += student["Score"]
avg = total / len(students)
print(avg)
     
print("Highestscore:", highestscore)
print("Higheststudent:",highestudent)



