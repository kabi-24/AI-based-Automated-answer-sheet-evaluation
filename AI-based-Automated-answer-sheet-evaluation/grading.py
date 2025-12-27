def assign_grade(score_percentage):
    if score_percentage >= 85:
        return "Excellent"
    elif score_percentage >= 70:
        return "Good"
    elif score_percentage >= 50:
        return "Average"
    else:
        return "Poor"