# This module runs the BMI function

'''
Body Mass Index - Input height in feet and inches. Input weight in pounds. Return BMI value and
category: Underweight = <18.5; Normal weight ! = 18.5–24.9; Overweight = 25–29.9; Obese = BMI
of 30 or greater (need to convert height and weight to metric values - see formula linked below) 
'''

METRIC_CONVERSION_FACTOR_WEIGHT = .45
METRIC_CONVERSION_FACTOR_HEIGHT = .025

def BMI(feet,inches,pounds):
    # First, verify that the data inputted is of the correct type
    if not isinstance(feet,int):
        raise TypeError('Argument feet must be passed as an integer')

    if not isinstance(inches,int):
        raise TypeError('Argument inches must be passed as an integer')

    if not isinstance(pounds,float):
        raise TypeError('Argument pounds must be passed as an float')

    # Next, convert to metric and calculate BMI
    calculatedBMI = calculate_BMI(feet, inches, pounds)
    # Classify person based on BMI
    classifiedBMI = classify_BMI(calculatedBMI)
    return "Your BMI is: " + str(calculatedBMI) + " and you are " + classifiedBMI

def calculate_BMI(feet, inches, pounds):
    metric_weight = pounds * METRIC_CONVERSION_FACTOR_WEIGHT
    metric_height = (feet*12 + inches) * METRIC_CONVERSION_FACTOR_HEIGHT
    return  round((metric_weight / (metric_height**2)), 1) 

def classify_BMI(calculated_BMI):
    if calculated_BMI < 18.5:
        return "Underweight"
    elif calculated_BMI >= 18.5 and calculated_BMI <= 24.9:
        return "Normal weight"
    elif calculated_BMI >= 25 and calculated_BMI <= 29.9:
        return "Overweight"
    elif calculated_BMI >= 30:
        return "Obese"
    else:
        return "Error calculating BMI"