W = int(input("Enter your weight(kg) : "))
H = float(input("Enter your height(m) : "))
BMI = W/(H*H)
print('Your BMI is %.1f '%BMI)
if BMI < 18.5:
    print("Under weight")
elif BMI < 25:
    print("Normal weight") 
elif BMI < 30:
    print("Overweight")
elif BMI >= 30:
    print("Obesity")
