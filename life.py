age = input("What's your current age? \n")
max_age = 90

age_in_int = int(age)
years_remaining = (max_age - age_in_int)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months until the max age which is 90 (this is for the exercise, I wanna live until 100)."

print(message)
