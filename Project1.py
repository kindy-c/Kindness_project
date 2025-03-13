# year = int(input("Enter a year: "))

# # Check if the year is a leap year
# if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
#  print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# check if a number is an even number
# number = int(input("Enter your number: "))
# if (number % 2 == 0):
#     print(f" {number} is an even number")
# else:
#     print(f"{number} is not an even number")

# Create a code to recruit personnels based on their ages and gender into various departments
# while True:
#     name = input("Enter applicant's name: ")
#     age = int(input("Enter applicant's age: "))
#     gender = input("Enter applicant's gender (male/female): ")
#     department = ""
    
#     if age < 18 or age > 50:
#         department = "Not Eligible"
#     else:
#         if gender.lower() == "male":
#             if age < 25:
#                 department = "Customer care"
#             elif age < 45:
#                 department = "Engineering"
#             else:
#                 department = "Security"
#         elif gender.lower() == "female":
#             if age < 31:
#                 department = "Customer care"
#             else:
#                 department = "Admin"

#     print(f"{name} has been assigned to the {department} department")
#     if department == "Not Eligible":
#         print(f"{name} is not eligible for employment")

#         response = input("Do you want to process another applicant?, yes/no: ")
#         if response.lower() == "no":
#             break

# Another variation to the code
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")

# if age < 18 or age > 50:
#     print(f"{name}, you are not qualified for this recruitment")
# else:
#     if (gender == "male" and age < 25) or (gender == "female" and age < 31):
#         print(f"{name}, you will be in the Customer care Department")
#     elif gender == "male" and age <= 45:
#         print(f"{name}, you are placed in the Engineering Department")
#     elif gender == "female" and age >= 31:
#         print(f"{name}, you are placed in the Admin Department")
#     else:
#         print(f"{name}, you are placed in the Security Department")
