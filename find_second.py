def second_highest(students):
    line = []
    student = []
    name = []
    points = []
    for line in students:    
        name.append(line[0])
        points.append(line[1])
    x = sorted(points, reverse = True)
    a = 0
    p = 0
    for line in x:
        if x[0] == x[a]:
            a += 1
            continue
        elif x[a] == x[a+1]: 
            p = x[a]
            a += 1
        else:
            break
    a = 0        
    for line in points:
        if line == p:
            print(name[a])
        a += 1


students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
second_highest(students)                    






            

