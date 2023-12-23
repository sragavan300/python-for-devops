import sys

listOfStudents = [ 1, 2, 33, "ragav", 5 ]
listOfAdmin = ("admin1", "admin2")

print("admin3" in listOfAdmin)
print(listOfAdmin[0:1])

#listOfStudents.append("karthi")

if "ragav" in listOfStudents:
    print('before remove success')
 
listOfStudents.remove(str("ragav"))

listOfStudents.sort()

listOfStudents.reverse()

print(listOfStudents[0:len(listOfStudents)])

if "ragav" in listOfStudents:
    print('after')
else:
    print('else after remove')




