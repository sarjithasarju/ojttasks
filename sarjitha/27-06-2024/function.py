def calculate_grades(student_scores):
    def average(scores):
        return sum(scores) / len(scores)
    
    def get_grade(avg_score):
        if avg_score >= 90:
            return 'A'
        elif avg_score >= 80:
            return 'B'
        elif avg_score >= 70:
            return 'C'
        elif avg_score >= 60:
            return 'D'
        else:
            return 'F'
    
    return {student: get_grade(average(scores)) for student, scores in student_scores.items()}

# Example usage
student_scores = {
    'Alice': [85, 92, 88],
    'Bob': [78, 81, 74],
    'Charlie': [95, 90, 93],
    'David': [60, 59, 62],
    'Eva': [50, 58, 52]
}

grades = calculate_grades(student_scores)
print(grades)
