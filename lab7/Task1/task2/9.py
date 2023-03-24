if __name__ == '__main__':
    students = []
    grades = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        grades.add(score)
    result = sorted(students, key=lambda x: (x[1], x[0]))
    second_grade = sorted(list(grades))[1]
    for x in result:
        if x[1] == second_grade:
            print(x[0])