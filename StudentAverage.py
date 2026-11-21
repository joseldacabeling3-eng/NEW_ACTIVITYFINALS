
print("=== STUDENT AVERAGE ===")

name = input("Student name: ")

math = float(input("Math grade: "))
english = float(input("English grade: "))
science = float(input("Science grade: "))

average = (math + english + science) / 3

print("\n=== STUDENT RESULT ===")
print("Name:", name)
print("Average:", round(average, 2))

if average >= 75:
    print("Status: PASSED")
else:
    print("Status: FAILED")
