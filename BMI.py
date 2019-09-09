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

    # Next, convert to metric
    metric_weight = pounds * METRIC_CONVERSION_FACTOR_WEIGHT
    metric_height = (feet*12 + inches) * METRIC_CONVERSION_FACTOR_HEIGHT

    result = metric_weight / (metric_height**2)  
    return result