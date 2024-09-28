# rite a Python program to create a list of 5 numbers. Add an element to the list, 
# remove one element, and find the maximum and minimum number in the list.
numbers: int = [11, 22, 33, 44, 55]
# add an element to the list
numbers.append(66)
print(numbers)
# remove element from the list
numbers.pop(4)
print(numbers)
# to find maximum numbers
maximum_number = max(numbers)
# to find minimum numbers
minimum_number = min(numbers)
print(minimum_number)
print(maximum_number)




# Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'], write a program to:
#  Access the first, middle, and last element of the list.
# Change the second element to 'blueberry'.
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# Access the first element
print(fruits[0])
# Access the middle element
print(fruits[2])
# Access the last element
print(fruits[-1])
# change the second element
fruits[-1] = 'blueberry' 
print(fruits) 


# Write a program that takes a list of student names as input, sorts the names in alphabetical order, and prints the sorted list.
student_names = ["Usman", "Ali", "Rehan", "Arslan", "Ahmad"]
student_names.sort()
print(student_names)

# rite a program that takes a list of integers and prints:
# The first 3 elements
# The last 2 elements
# The entire list in reverse order
numbers = ["11", "22", "33", "44", "55", "66", "77", "88",]
# the first three element
print(numbers[:3])
# The last two element
print(numbers[:-2])
# The entire list in reverse order
print(numbers[::-1])


# rite a Python program that removes all duplicates from a given list and prints the new list without duplicates.
numbers : list[int] = [1, 2, 3, 4, 5 ,3, 4, 5 ,10, 2 ]
numbers = list (set(numbers))


#  Create a dictionary where the keys are the names of 5 different countries and the values are their capitals. 
#  Write a program to display all the countries and their capitals.
countries = {"Pakistan" : "Islamabd",
             "India" : "Delhi",
             "USA" : "Washington",
             "Germany" : "Berlin",
             "Punjab" : "Lahore"
             }
print(countries)

# - Write a program to update the 'grade' value to 'A', and add a new key-value pair for 'major' with the value 'Computer Science'.
student = {'name': 'John', 'age': 22, 'grade': 'B'}
# add a new key
student.update({"major" : "Computer Science"})
# update the grade 
student["grade"] = "A"
print(student)

# prompt: te a program that creates a dictionary where the keys are subjects (e.g., 'Math', 'Science') and the values are lists of marks. Add marks for 3 subjects, and print the average marks for each subject.

def calculate_average(marks):
  total = sum(marks)
  return total / len(marks) if marks else 0

subject_marks = {
    'Math': [85, 90, 95],
    'Science': [70, 80, 90],
    'English': [80, 85, 92]
}

for subject, marks in subject_marks.items():
  average_marks = calculate_average(marks)
  print(f'The average marks for {subject} is: {average_marks}')





