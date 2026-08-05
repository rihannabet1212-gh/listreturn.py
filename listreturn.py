list = []
for i in range(3):
    names=input("name: ")
    score=float(input("score: "))
    list.append({
        "names" : names ,
        "score" : score
                })
print(list)
def an(a):

    if a>=90:
     return("yayyyyyyyy")
    elif a>=50:
       return("pass")
    else :
       return("fail")
result=an(score)
print(result)



