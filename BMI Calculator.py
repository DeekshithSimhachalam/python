weight = float(input('Please enter your weight:'))
height = float(input('Please enter your height in Meters:'))
BMI = weight/height**2
if BMI <= 18.5:
    print('underweight')
elif BMI >= 18.5 and BMI < 25:
    print('Normal')
elif BMI >= 25 and BMI < 30:
    print('Overweight')
else:
    print('Obesity')