def bmi(weight, height):
    #your code here
    total = weight / (height ** 2)
    if total <= 18.5:
        return "Underweight"
    elif total <= 25.0:
        return "Normal"
    elif total <= 30.0:
        return "Overweight"
    else:
        return "Obese"

