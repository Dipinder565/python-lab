courses = ["Physics I",
           "Calculus I",
           "History I",
           "Introduction to programming",
           "Biology I",
           "Linear algebra",
           "Microeconimics",
           "Chemistry"]
print(courses)


#2 list 
#orignal list 
print("Orignal list:")
print(courses)

#2.1 sorted lists
print("\nAlphabetical order:")
print(sorted(courses))

#2.2 reverse list
print("\nreverse alphabetic lists:")
print(sorted(courses,reverse=True))

#2.3 sort
courses.sort()
print(courses)
courses.reverse()
print("\nReversed list:")
print(courses)

courses.reverse()
print("\nBack to original:")
print(courses)

#2.4 replace a course 
# replace first course
courses[0] = "Psychology I"

print("\nUpdated list after replacement:")
print(courses)
# add courses
courses.insert(0, "English Composition I")   # beginning
courses.insert(2, "Linear Algebra")          # middle
courses.append("Philosophy")                 # end

print("\nAfter adding new courses:")
print(courses)
# remove 4 courses
removed1 = courses.pop()
removed2 = courses.pop()
removed3 = courses.pop()
removed4 = courses.pop()

print("\nRemoved courses:")
print(removed1, removed2, removed3, removed4)

print("\nRemaining courses:")
print(courses)set

#tuple and list
course_data = [
    (1, "Programming"),
    (2, "Math"),
    (3, "Physics")
]

course_names = []

for course in course_data:
    course_names.append(course[1])

print("\nCourse names:")
print(course_names)



#session4 

# 1 Data (List of courses)
courses = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
]

# 2 Loop (runs again and again)
while True:

    # 3 User Input
    user_input = input("\nEnter course ID (1-15) or 0/quit to exit: ")

    # 4 Exit condition
    if user_input.lower() == "quit" or user_input == "0":
        print("Program exited.")
        break

    # 5 Check if input is number
    if not user_input.isdigit():
        print("Invalid input. Enter a number.")
        continue

    # 6 Convert to integer
    course_id = int(user_input)

    # 7 Check range
    if course_id < 1 or course_id > 15:
        print("Course ID must be between 1 and 15.")
        continue

    # 8 Search for course
    found = False

    for course in courses:
        if course_id == course[0]:

            # 9 Display output
            print("\nCourse ID:", course[0])
            print("Course Name:", course[1])
            print("Department:", course[2])
            print("Prerequisites:", course[3])

            found = True
            break

    # 10 If not found
    if not found:
        print("Course not found.")
        