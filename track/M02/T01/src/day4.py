# Read the number
number = int(input("enter the number: "))
# Check whether the number is positive, negative or zero
if number > 0:
    print("Number is Positive")
elif number < 0:
    print("Number is Negative")
else:
    print("Number is Zero")



# Read marks, attendance and project completion status
marks = int(input())
attendence = int(input())
project_complition = (input())
# Check the academic requirements
if marks >= 60 and attendence >= 75:
    if project_complition == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
# Check the project completion status
else:
    print("Not Eligible")



# Read the value of n
n = int(input())
# Initialize the counter and total
counter = 1
total = 0
# Calculate the total using a while loop
while counter <= n:
    total = total + counter
    counter = counter + 1
# Display the total
print(f"Total: {total}")



# Read the number and word
N = int(input())
word = input()
# Print the number sequence
print("Numbers: ")
for i in range(1, N+1):
    print(i)
# Print the characters
print("Characters: ")
for char in word:
    print(char)