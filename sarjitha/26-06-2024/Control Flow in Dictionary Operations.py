def calculate_grades(scores_dict):
    def get_letter_grade(average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    grades_dict = {}
    for student, scores in scores_dict.items():
        average_score = sum(scores) / len(scores)
        grades_dict[student] = get_letter_grade(average_score)
    
    return grades_dict

# Example usage:
student_scores = {
    'Alice': [85, 92, 78],
    'Bob': [88, 73, 95],
    'Charlie': [60, 65, 58],
    'Diana': [92, 93, 91],
    'Eve': [55, 50, 45]
}

grades = calculate_grades(student_scores)
print(grades)
