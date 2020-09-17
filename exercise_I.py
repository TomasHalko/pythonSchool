studentNames = ['Tom', 'Sam', 'Vlad', 'Liisa']

newStudent = input("Enter a new student name: ")

studentNames.append(newStudent)

print(f"We have {len(studentNames)} students in total. Welcome to our latest student {studentNames[-1]}!")