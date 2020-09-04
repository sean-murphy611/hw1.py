#declare variables
A = 4.0
Aminus = 3.67
Bplus = 3.33
B = 3.0
Bminus = 2.67
Cplus = 2.33
C = 2.0
D = 1.0 
F = 0.0



#Ask for grade
gradepoint1 = input(print("Enter your course 1 letter grade: "))
credit1 = str(input(print("Enter your course 1 credit: ")))
if gradepoint1 == "A":
  grade1 = str(A)
elif gradepoint1 =="A-":
  grade1 = str(Aminus)
elif gradepoint1 == "B+":
  grade1 = str(Bplus)
elif gradepoint1 == "B":
  grade1 = str(B)
elif gradepoint1 == "B-":
  grade1 = str(Bminus)
elif gradepoint1 == "C+":
  grade1 = str(Cplus)
elif gradepoint1 == "C":
  grade1 = str(C)
elif gradepoint1 == "D":
  grade1 = str(D)
else:
  grade1 = str(F)
print(f"Grade point for course 1 is: {grade1}")

gradepoint2 = input(print("Enter your course 2 letter grade: "))
credit2 = str(input(print("Enter your course 2 credit: ")))
if gradepoint2 == "A":
  grade2 = str(A)
elif gradepoint2 =="A-":
  grade2 = str(Aminus)
elif gradepoint2 == "B+":
  grade2 = str(Bplus)
elif gradepoint2 == "B":
  grade2 = str(B)
elif gradepoint2 == "B-":
  grade2 = str(Bminus)
elif gradepoint2 == "C+":
  grade2 = str(Cplus)
elif gradepoint2 == "C":
  grade2 = str(C)
elif gradepoint2 == "D":
  grade2 = str(D)
else:
  grade2 = str(F)
print(f"Grade point for course 2 is: {grade2}")

gradepoint3 = input(print("Enter your course 3 letter grade: "))
credit3 = str(input(print("Enter your course 3 credit: ")))
if gradepoint3 == "A":
  grade3 = str(A)
elif gradepoint3 =="A-":
  grade3 = str(Aminus)
elif gradepoint3 == "B+":
  grade3 = str(Bplus)
elif gradepoint3 == "B":
  grade3 = str(B)
elif gradepoint3 == "B-":
  grade3 = str(Bminus)
elif gradepoint3 == "C+":
  grades3 = str(Cplus)
elif gradepoint3 == "C":
  grade3 = str(C)
elif gradepoint3 == "D":
  grade3 = str(D)
else:
  grade3 = str(F)
print(f"Grade point for course 3 is: {grade3}")

gpa = (grade1*credit1 +grade2*credit2 + grade3*credit3)/(credit1+credit2+credit3)

float(print(f"Your GPA is: {gpa}"))
