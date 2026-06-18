students = []

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = input("Enter choice: ")
    
    # 1. ADD STUDENT
    if choice == "1":
        print("\nEnter student details:")
        s_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth: ")
        subs = input("Subjects: ")
        
        row = [s_id, name, age, grade, dob, subs]
        students.append(row)
        print("Student added!")
            
    # 2. DISPLAY ALL STUDENTS
    elif choice == "2":
        print("\n--- All Students ---")
        for s in students:
            print(f"ID: {s[0]} | Name: {s[1]} | Age: {s[2]} | Grade: {s[3]} | Subjects: {s[5]}")

    # 3. UPDATE STUDENT
    elif choice == "3":
        search_id = input("\nEnter Student ID to update: ")
        for s in students:
            if s[0] == search_id:
                print(f"Updating {s[1]}...")
                
                new_name = input(f"New Name ({s[1]}): ")
                if new_name != "": s[1] = new_name
                    
                new_age = input(f"New Age ({s[2]}): ")
                if new_age != "": s[2] = new_age
                    
                new_grade = input(f"New Grade ({s[3]}): ")
                if new_grade != "": s[3] = new_grade
                    
                new_dob = input(f"New DOB ({s[4]}): ")
                if new_dob != "": s[4] = new_dob
                    
                new_subs = input(f"New Subjects ({s[5]}): ")
                if new_subs != "": s[5] = new_subs
                print("Updated successfully!")

    # 4. DELETE STUDENT
    elif choice == "4":
        search_id = input("\nEnter Student ID to delete: ")
        for s in students:
            if s[0] == search_id:
                students.remove(s)
                print("Deleted successfully!")
                break

    # 5. DISPLAY SUBJECTS OFFERED
    elif choice == "5":
        print("\nSubjects Offered")
        for s in students:
            print(s[5])

    # 6. EXIT
    elif choice == "6":
        print("Goodbye!")
        break
