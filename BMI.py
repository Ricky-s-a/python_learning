# define value
h = float(input("Hight?(cm): "))
w = float(input("Weight?(kg): "))

# calcurate
bmi = round(w / (h/100.0) ** 2, 2)
bmi
if bmi < 18.5:
    result = "underweight"
elif bmi >= 18.5 and bmi < 25:
    result = "healthy weight"
elif bmi >= 25.0 and bmi < 30:
    result = "overweight"
else:
    result = "obesity"
result

# show the result
print("Your BMI is " + str(bmi) + ".\n"
    + "Your BMI falls in " + result + " range.")
