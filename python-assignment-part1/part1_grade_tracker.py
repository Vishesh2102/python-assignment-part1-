# ==========================================
# Task 1: Data Parsing & Profile Cleaning
# ==========================================

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    # Cleaning the name using strip and title case as taught in class
    clean_name = student["name"].strip().title()
    
    # Converting roll from string to integer
    clean_roll = int(student["roll"])
    
    # Converting the marks string into a list of integers
    # First I split them by the comma, then loop through to convert each one
    temp_marks = student["marks_str"].split(", ")
    clean_marks = []
    for m in temp_marks:
        clean_marks.append(int(m))
    
    # Validating name: Check if each word is only alphabetic
    is_valid = True
    for word in clean_name.split():
        if not word.isalpha():
            is_valid = False
            break
            
    validation_icon = "✓ Valid name" if is_valid else "✗ Invalid name"
    
    # Saving to a new dictionary
    cleaned_entry = {
        "name": clean_name, 
        "roll": clean_roll, 
        "marks": clean_marks
    }
    cleaned_students.append(cleaned_entry)
    
    # Printing the formatted profile card
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {clean_marks}")
    print(f"Status  : {validation_icon}")
    print("================================")

# Printing variations for roll 103
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nRoll 103 Upper: {s['name'].upper()}")
        print(f"Roll 103 Lower: {s['name'].lower()}\n")


# ==========================================
# Task 2: Marks Analysis Using Loops
# ==========================================

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"--- Analysis for {student_name} ---")

# Using a for loop to assign grades to each subject
for i in range(len(subjects)):
    score = marks[i]
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"{subjects[i]}: {score} - Grade: {grade}")

# Calculations
total_marks = sum(marks)
avg_marks = total_marks / len(marks)

# Finding high/low using index matching
high_val = max(marks)
high_sub = subjects[marks.index(high_val)]

low_val = min(marks)
low_sub = subjects[marks.index(low_val)]

print(f"\nTotal: {total_marks}")
print(f"Average: {avg_marks:.2f}")
print(f"Highest: {high_sub} ({high_val})")
print(f"Lowest: {low_sub} ({low_val})")

# While loop for new entries with error handling (like the 'order' example from class)
print("\n--- Add New Subjects ---")
added_count = 0
while True:
    new_sub = input("Enter subject name (or 'done'): ").strip()
    if new_sub.lower() == "done":
        break
        
    try:
        new_score = int(input(f"Enter marks for {new_sub} (0-100): "))
        if 0 <= new_score <= 100:
            subjects.append(new_sub)
            marks.append(new_score)
            added_count += 1
        else:
            print("Warning: Marks must be between 0 and 100.")
    except ValueError:
        print("Warning: Please enter a valid number.")

final_avg = sum(marks) / len(marks)
print(f"New subjects added: {added_count}")
print(f"Updated average: {final_avg:.2f}\n")


# ==========================================
# Task 3: Class Performance Summary
# ==========================================

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print(f"{'Name':<18} | {'Average':<7} | Status")
print("-" * 40)

pass_total = 0
fail_total = 0
all_averages = []
top_name = ""
top_avg = 0

for name, s_marks in class_data:
    avg = round(sum(s_marks) / len(s_marks), 2)
    status = "Pass" if avg >= 60 else "Fail"
    
    # Update class stats
    all_averages.append(avg)
    if status == "Pass":
        pass_total += 1
    else:
        fail_total += 1
        
    if avg > top_avg:
        top_avg = avg
        top_name = name
        
    print(f"{name:<18} |  {avg:>6.2f}  | {status}")

class_overall_avg = sum(all_averages) / len(all_averages)

print("-" * 40)
print(f"Passed: {pass_total} | Failed: {fail_total}")
print(f"Class Topper: {top_name} ({top_avg})")
print(f"Class Average: {class_overall_avg:.2f}\n")


# ==========================================
# Task 4: String Manipulation Utility
# ==========================================

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Strip whitespace
clean_essay = essay.strip()
print(f"1. Cleaned: {clean_essay}")

# Step 2: Title Case
print(f"2. Title Case: {clean_essay.title()}")

# Step 3: Count "python" (using lower() to make it case-insensitive)
p_count = clean_essay.lower().count("python")
print(f"3. Occurrences of 'python': {p_count}")

# Step 4: Replace
replaced_text = clean_essay.replace("python", "Python 🐍")
print(f"4. Replaced Text: {replaced_text}")

# Step 5: Split into list
sentences = clean_essay.split(". ")
print(f"5. Sentences List: {sentences}")

# Step 6: Formatting sentences (using enumerate like the file-reading example)
print("\n6. Formatted Sentences:")
for i, line in enumerate(sentences, 1):
    # Cleaning any extra bits and ensuring it ends with a period
    current_sentence = line.strip()
    if not current_sentence.endswith("."):
        current_sentence += "."
    print(f"{i}. {current_sentence}")