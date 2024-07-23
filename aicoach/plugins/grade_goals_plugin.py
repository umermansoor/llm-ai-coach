from typing import Annotated
from semantic_kernel.functions import kernel_function

class GradesPlugin:
    def __init__(self):
        self.courses = {
            'Math': [],
            'Physics': [],
            'Chemistry': [],
            'Computer Science': []
        }

        self.set_target_grademax_score(600)
        self.add_grade('Math', 80)
        self.add_grade('Math', 90)
        self.add_grade('Physics', 75)
        self.add_grade('Chemistry', 80)
        self.add_grade('Computer Science', 95)
        self.add_grade('Computer Science', 100)

    @kernel_function(
        name="set_target_grademax_score",
        description="Sets the target GradeMax score for the student. GradeMax is the overall academic grade score calculated from the average of all courses and various other factors",
    )
    def set_target_grademax_score(
        self,
        target_grademax_score: Annotated[float, "The target GradeMax score"],
    ) -> Annotated[str, "Confirmation message"]:
        """Sets the GradeMax that the student is aiming for."""
        if target_grademax_score < 50:
            raise ValueError("Target GradeMax score must be at least 50")
        self.target_grademax_score = target_grademax_score
        return f"Target overall grade set to {target_grademax_score}"
    
    @kernel_function(
        name="get_target_grademax_score",
        description="Gets the target GradeMax score",
    )
    def get_target_grademax_score(
            self) -> Annotated[int, "The target GradeMax score"]:
        """Gets the target GradeMax score."""
        return f"Target GradeMax score is {self.target_grademax_score}"
    
    @kernel_function(
        name="calculate_grademax_score",
        description="Calculates the overall GradeMax score",
    )
    def calculate_grademax_score(
        self,
    ) -> Annotated[float, "The overall GradeMax score"]:
        """Calculates the overall GradeMax score."""

        # Take weighted average of all courses
        total_score = 0
        total_weight = 0
        for course, grades in self.courses.items():
            if course == 'Computer Science':
                weight = 1.2 # CSC is weighted heavily
            else:
                weight = 1
            total_score += sum(grades) / len(grades) * weight
            total_weight += weight
        average_score = total_score / total_weight

        # Calculate the GradeMax score
        grademax_score = average_score * 10
        return grademax_score
    
    @kernel_function(
        name="get_list_of_courses",
        description="Gets a list of all courses that the student is taking",
    )
    def get_list_of_courses(
        self,
    ) -> Annotated[list, "A list of all courses"]:
        """Gets a list of all courses."""
        return list(self.courses.keys())

    @kernel_function(
        name="add_grade",
        description="Adds a grade to a specified course",
    )
    def add_grade(
        self,
        course: Annotated[str, "The course name"],
        grade: Annotated[float, "The grade to add"],
    ) -> Annotated[str, "Confirmation message"]:
        """Adds a grade to a specified course."""
        if course in self.courses:
            self.courses[course].append(grade)
            return f"Added grade {grade} to {course}"
        else:
            raise ValueError(f"Course {course} is not recognized.")
        
    @kernel_function(
        name="get_course_grades",
        description="Gets the grades for a specified course",
    )
    def get_course_grades(
        self,
        course: Annotated[str, "The course name"],
    ) -> Annotated[list, "A list of grades for the specified course"]:
        """Gets the grades for a specified course."""
        if course in self.courses:
            return self.courses[course]
        else:
            raise ValueError(f"Course {course} is not recognized. Check the list of courses that the student is taking first.")


