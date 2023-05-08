two_digits_nb = input("Give me 2 digit numbers and the output will be the sum of it: ")

# print(type(two_digits_nb))

first_nb = int(two_digits_nb[0])
second_nb = int(two_digits_nb[1])

print(first_nb + second_nb)

print("--Start BMI(Body Mass Index) calculator")

height = input("Enter your height in meters: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) /(float(height) ** 2)

print(int(bmi))

print("Understand F Strings")

score = 0
height = 1.5
isWinning = True

print(f"your score is {score}, your height is {height} and, you are winning is {isWinning}")