import os

students = []
courses = []  
marks = {}

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def input_num_of_students():
    while True:
        try:
            n = int(input("Enter number of students: "))
            if (n > 0):
                return n
            else: 
                print("Please enter a positive number.")
        except:
            print("Invalid input")

def input_students_info():
    student_id = input("Enter student id: ") 
    name = input("Enter student name: ")
    dob = input("Enter student dob: ")

    student = (student_id, name, dob)
    students.append(student)
    print(f"Student {name} successfully added\n")

def input_number_of_courses():
    course_id = input("Enter course id: ")
    name = input("Enter course name: ")

    course = (course_id, name)
    courses.append(course)
    
    if course_id not in marks:
        marks[course_id] = {}

    print(f"Course {name} successfully added\n")

def input_mark_course():
    if not courses:
        print("No course available, please add courses first\n")
        input("Press Enter to continue...")
        return  
    
    if not students:
        print("No student available, please add student first\n")
        input("Press Enter to continue...")
        return 

    print("Available course: ")
    for i in range(len(courses)):
        course_id, course_name = courses[i]
        print(f"{i+1}. {course_name} (ID: {course_id})") 

    try:
        choice = int(input("\nSelect course: "))
        if 1 <= choice <= len(courses):
            course_id, course_name = courses[choice-1]
            print(f"\nEnter mark for this course: {course_name}\n")
            
            for student_id, student_name, _ in students:
                while True:
                    try:
                        mark = float(input(f"Enter mark for {student_name} (ID: {student_id}): "))
                        if 0 <= mark <= 20:
                            marks[course_id][student_id] = mark
                            break 
                        print("Mark must be between 0 and 20.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            print(f"Mark for {course_name} successfully saved\n")
        else: 
            print("Invalid choice\n")
            input("Press Enter to continue...")
    except ValueError:
        print("Invalid input.\n")
        input("Press Enter to continue...")

def list_courses():
    if not courses:
        print("No courses available\n")
        input("Press Enter to continue...")
        return
    
    print("\nCourse List: \n")
    for course_id, course_name in courses: 
        print(f"Name: {course_name} | ID: {course_id}\n")
    input("Press Enter to continue...")

def list_student():
    if not students:
        print("No students available\n")
        input("Press Enter to continue...")
        return
    print("\nStudent list: \n")
    for student_id, name, dob in students:
        print(f"ID: {student_id} | Name: {name} | DOB: {dob}\n")
    input("Press Enter to continue...")

def show_student_mark():
    if not courses: 
        print("No courses available\n")
        input("Press Enter to continue...")
        return
    
    print("\nAvailable Course: \n")
    for i in range(len(courses)):
        course_id, course_name = courses[i]
        print(f"{i+1}. {course_name} (ID: {course_id})") 

    try:
        choice = int(input("Select course number: "))
        if 1 <= choice <= len(courses):
            course_id, course_name = courses[choice-1]

            print(f"Mark for course: {course_name} (ID: {course_id})")

            if course_id not in marks or not marks[course_id]:
                print("No marks available for this courses\n")
            else:
                counter = 1
                for student_id, name, _ in students:
                    if student_id in marks[course_id]:
                        mark = marks[course_id][student_id]
                        print(f"{counter}. {name} | {student_id} | {mark:.2f}")
                    else:
                        print(f"{counter}. {name} | {student_id} | Null")
                    counter += 1 
            input("Press Enter to continue...")
        else: 
            print("Invalid choice.\n")
            input("Press Enter to continue...")
    except ValueError: 
        print("Invalid input\n")
        input("Press Enter to continue...")

def menu():
    print("\n" + "=" * 50)
    print("STUDENT MARK MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks for a course")
    print("4. List all courses")
    print("5. List all students")
    print("6. Show student marks for a course")
    print("0. Exit")
    print("=" * 50)

def main():
    while True:
        clear_screen() 
        menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            n = input_num_of_students()  
            for i in range(n):
                print(f"\n--- Student {i + 1} ---")
                input_students_info()  
            input("Press Enter to continue...")  
        
        elif choice == "2":
            n = int(input("Enter number of courses: "))  
            for i in range(n):
                print(f"\n--- Course {i + 1} ---")
                input_number_of_courses()  
            input("Press Enter to continue...")  
        elif choice == "3":
            input_mark_course()  
            input("Press Enter to continue...") 
        
        elif choice == "4":
            list_courses()
        
        elif choice == "5":
            list_student() 

        elif choice == "6":
            show_student_mark() 
        
        elif choice == "0":
            print("Goodbye!\n")
            break
        
        else:
            print("Invalid choice. Please try again.\n")
            input("Press Enter to continue...") 

if __name__ == "__main__":
    main()
