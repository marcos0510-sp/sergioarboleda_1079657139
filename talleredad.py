while True:
    students = []

    i = 0
    while i < 5:
        while True:
            name = input("Nombre: ")
            try:
                age = int(input("Edad: "))
                grade = float(input("Calificación: "))
                if 5 <= age <= 100 and 0 <= grade <= 5:
                    students.append({"name": name, "age": age, "grade": grade})
                    break
                else:
                    print("Datos inválidos. La edad debe estar entre 5 y 100, y la calificación entre 0 y 5.")
            except ValueError:
                print("Por favor, ingresa números válidos para edad y calificación.")
        i += 1

    # Encontrar el estudiante con la calificación más alta
    if students:
        max_student = max(students, key=lambda x: x["grade"])
        print(f"El estudiante con la calificación más alta es {max_student['name']} con {max_student['grade']}")

        # Encontrar el estudiante con la calificación más baja
        min_student = min(students, key=lambda x: x["grade"])
        print(f"El estudiante con la calificación más baja es {min_student['name']} con {min_student['grade']}")

        # Calcular el promedio de calificaciones
        average_grade = sum(student["grade"] for student in students) / len(students)
        print(f"La calificación promedio de todos los estudiantes es {average_grade:.2f}")

        # Preguntar si desea registrar otro grupo de estudiantes
        respuesta = input("¿Deseas registrar otro grupo de 5 estudiantes? (s/n): ")
        if respuesta.lower() != 's':
            break
    else:
        print("No se registraron estudiantes válidos.")
        break
