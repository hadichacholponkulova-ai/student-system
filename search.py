def search_student(name, student):
    for student in students:
        if student == name:
            return student
    return None