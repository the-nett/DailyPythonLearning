# Project Description
# For this project, your task is to perform some categorization of dictionary data. Create a .py script and paste the following dictionary there. The dictionary contains student grades.

grades = {
    "Alice": 78,
    "Bob": 42,
    "Charlie": 65,
    "Diana": 49,
    "Eve": 90
}
# Add some code after the above dictionary. The code should create a new dictionary that 
# categorizes students into "Pass" or "Fail" based on their grades. Consider a grade of 50 or higher as "Pass" 
# and below 50 as "Fail." Once you create a dictionary, use a for-loop to iterate over the new dictionary and 
# print out each pair of key and value as below:

validation_grades = {}

for name, grade in grades.items():
    if grade >= 50:
        validation_grades[name] = "Pass"
    else:
        validation_grades[name] = "Fail"


for name, state in validation_grades.items():
    print(f"{name}: {state}")
