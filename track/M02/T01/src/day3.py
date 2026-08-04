#convert to different data types
age_text = "21"
course_fee_text = "499.50"
attempts = 3
# Convert the values here
age_text = int(age_text)
course_fee_text = float(course_fee_text)
attempts = str(attempts)
# Display the converted values and their data types
print(age_text)
print(type(age_text))
print(course_fee_text)
print(type(course_fee_text))
print(attempts)
print(type(attempts))


#correcting mistakes
current_age = 21
next_age = (current_age) + 1
print(f"Age next year: {next_age}")


# Read and convert the student details
student_name = str(input())
age = int(input())
rating = float(input())
# Display the values
print(f"Student: {student_name}")
print(f"Age: {age}")
print(f"Rating: {rating}")
# Display the data types
print(type(student_name))
print(type(age))
print(type(rating))


#Calculate Division & Floor Division
first_number = int(input())
second_number = int(input())
# Write your code here
division = first_number / second_number
floorDivision = first_number // second_number
print(f"{division}")
print(f"{floorDivision}")


#Add Two Numbers
# Read the numbers
first_number = int(input())
second_number = int(input())
# Calculate the sum
sum_result = first_number + second_number
# Display the result
print(f"Sum: {sum_result}")