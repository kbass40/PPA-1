# This module runs the Retirement Function

'''
Retirement - Input user's current age, annual salary , percentage saved (employer matches 35% of
savings). Input desired retirement savings goal. Output what age savings goal will be met. You can
assume death at 100 years (therefore, indicate if the savings goal is not met ). 
'''

def Retirement(age,salary,saved,goal):
    # First, verify that the data inputted is of the correct type
    if not isinstance(age,int):
        raise TypeError('Argument age must be passed as an integer')
    if not isinstance(salary,int):
        raise TypeError('Argument salary must be passed as an integer')
    if not isinstance(saved,float):
        raise TypeError('Argument saved percentage must be passed as an float of type ##%')
    if not isinstance(goal,int):
        raise TypeError('Argument goal must be passed as an integer')

def total_saved_per_year(salary):
    return salary * 1.35