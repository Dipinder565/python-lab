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
