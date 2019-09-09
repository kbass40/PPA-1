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
    
    # Next we test if the data makes sense given the domain
    # 0 feet is allowed but nothing past 8 feet cause that matches the highest person who's ever lived
    if feet < 0 or feet > 8:
        raise RuntimeError('Argument feet cannot be less than 0 or greater than 8!')

    if inches < 0 or inches > 11:
        raise RuntimeError('Argument inches cannot be less than 0 or greater than 11!')

    if pounds <= 0 :
        raise RuntimeError('Argument pounds cannot be less than or equal to 0!')


    # Next, convert to metric and calculate BMI
    calculatedBMI = calculate_BMI(feet, inches, pounds)
    return calculatedBMI

def calculate_BMI(feet, inches, pounds):
    metric_weight = pounds * METRIC_CONVERSION_FACTOR_WEIGHT
    metric_height = (feet*12 + inches) * METRIC_CONVERSION_FACTOR_HEIGHT
    return  round((metric_weight / (metric_height**2)), 1) 