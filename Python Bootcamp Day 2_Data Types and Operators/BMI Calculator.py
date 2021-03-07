#BMI Calculator

#obtain height and weight
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

###bmi = kg/(m^2)

#insert provided variables into equation
bmi = float(weight)/float(height)**2

#print result
print("Your BMI is "+str(round(bmi,0)))










