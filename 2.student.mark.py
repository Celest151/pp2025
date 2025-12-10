import os
from typing import Dict, List, Optional


class Student:
    def __init__(self, student_id: str, name: str, dob: str):
        self._student_id = student_id
        self._name = name
        self._dob = dob
    
    @property
    def student_id(self) -> str:
        return self._student_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def dob(self) -> str:
        return self._dob
    
    def __str__(self) -> str:
        return f"ID: {self._student_id} | Name: {self._name} | DOB: {self._dob}"
    
    @classmethod
    def input(cls) -> 'Student':
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        return cls(student_id, name, dob)


class Course:
    def __init__(self, course_id: str, name: str):
        self._course_id = course_id
        self._name = name
        self._marks: Dict[str, float] = {}
    
    @property
    def course_id(self) -> str:
        return self._course_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def marks(self) -> Dict[str, float]:
        return self._marks
    
    def add_mark(self, student_id: str, mark: float) -> None:
        if 0 <= mark <= 20:
            self._marks[student_id] = mark
        else:
            raise ValueError("Mark must be between 0 and 20")
    
    def get_mark(self, student_id: str) -> Optional[float]:
        return self._marks.get(student_id)
    
    def __str__(self) -> str:
        return f"Name: {self._name} | ID: {self._course_id}"
    
    @classmethod
    def input(cls) -> 'Course':
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        return cls(course_id, name)


class StudentMarkSystem:
    def __init__(self):
        self._students: List[Student] = []
        self._courses: List[Course] = []
    
    def add_student(self, student: Student) -> None:
        self._students.append(student)
    
    def add_course(self, course: Course) -> None:
        self._courses.append(course)
    
    def get_students(self) -> List[Student]:
        return self._students
    
    def get_courses(self) -> List[Course]:
        return self._courses
    
    def input_students(self) -> None:
        n = self._input_positive_number("Enter number of students: ")
        for i in range(n):
            print(f"\n--- Student {i + 1} ---")
            student = Student.input()
            self.add_student(student)
            print(f"Student {student.name} successfully added\n")
        input("Press Enter to continue...")
    
    def input_courses(self) -> None:
        n = self._input_positive_number("Enter number of courses: ")
        for i in range(n):
            print(f"\n--- Course {i + 1} ---")
            course = Course.input()
            self.add_course(course)
            print(f"Course {course.name} successfully added\n")
        input("Press Enter to continue...")
    
    def input_marks(self) -> None:
        if not self._courses:
            print("No course available, please add courses first\n")
            input("Press Enter to continue...")
            return
        
        if not self._students:
            print("No student available, please add student first\n")
            input("Press Enter to continue...")
            return
        
        course = self._select_course()
        if course is None:
            return
        
        print(f"\nEnter mark for this course: {course.name}\n")
        
        for student in self._students:
            while True:
                try:
                    mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
                    if 0 <= mark <= 20:
                        course.add_mark(student.student_id, mark)
                        break
                    print("Mark must be between 0 and 20.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        print(f"Mark for {course.name} successfully saved\n")
        input("Press Enter to continue...")
    
    def list_courses(self) -> None:
        if not self._courses:
            print("No courses available\n")
            input("Press Enter to continue...")
            return
        
        print("\nCourse List:\n")
        for course in self._courses:
            print(course)
            print()
        input("Press Enter to continue...")
    
    def list_students(self) -> None:
        if not self._students:
            print("No students available\n")
            input("Press Enter to continue...")
            return
        
        print("\nStudent list:\n")
        for student in self._students:
            print(student)
            print()
        input("Press Enter to continue...")
    
    def show_marks(self) -> None:
        if not self._courses:
            print("No courses available\n")
            input("Press Enter to continue...")
            return
        
        course = self._select_course()
        if course is None:
            return
        
        print(f"\nMark for course: {course.name} (ID: {course.course_id})\n")
        
        if not course.marks:
            print("No marks available for this course\n")
        else:
            for i, student in enumerate(self._students, 1):
                mark = course.get_mark(student.student_id)
                if mark is not None:
                    print(f"{i}. {student.name} | {student.student_id} | {mark:.2f}")
                else:
                    print(f"{i}. {student.name} | {student.student_id} | Null")
        
        input("Press Enter to continue...")
    
    def _select_course(self) -> Optional[Course]:
        print("Available courses:\n")
        for i, course in enumerate(self._courses, 1):
            print(f"{i}. {course.name} (ID: {course.course_id})")
        
        try:
            choice = int(input("\nSelect course: "))
            if 1 <= choice <= len(self._courses):
                return self._courses[choice - 1]
            else:
                print("Invalid choice\n")
                input("Press Enter to continue...")
                return None
        except ValueError:
            print("Invalid input\n")
            input("Press Enter to continue...")
            return None
    
    @staticmethod
    def _input_positive_number(prompt: str) -> int:
        while True:
            try:
                n = int(input(prompt))
                if n > 0:
                    return n
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input")
    
    @staticmethod
    def _clear_screen() -> None:
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def run(self) -> None:
        while True:
            self._clear_screen()
            self._show_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.show_marks()
            elif choice == "0":
                print("Goodbye!\n")
                break
            else:
                print("Invalid choice. Please try again.\n")
                input("Press Enter to continue...")
    
    @staticmethod
    def _show_menu() -> None:
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
    system = StudentMarkSystem()
    system.run()

if __name__ == "__main__":
    main()