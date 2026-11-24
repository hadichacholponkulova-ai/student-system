from students import add_student, show_students
from search import search_student

add_student("Иванов Иван")
add_student("Петров Петр")
result = search_student("Иванов Иван", ["Иванов Иван", "Петров Петр"])
print("Найден:", result)