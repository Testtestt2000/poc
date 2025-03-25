def determine_grade(score):
    if 90 <= score <= 100:
        return "A", "With Compliments"
    elif 80 <= score <= 89:
        return "B", "Very Satisfy"
    elif 70 <= score <= 79:
        return "C", "Satisfying"
    elif 60 <= score <= 69:
        return "D", "Not Satisfactory"
    elif 0 <= score <= 59:
        return "E", "Not PASS"
    else:
        return None, "Invalid Score"

# Input score from user
score = int(input("Enter the score: "))

# Determine grade and predicate
grade, predicate = determine_grade(score)

# Display result
if grade:
    print(f"Grade: {grade}, Predicate: {predicate}")
else:
    print(predicate)