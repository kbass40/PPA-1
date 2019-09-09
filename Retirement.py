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

    # calculate amount saved per year after employer matching
    totalSaved = total_saved_per_year(salary, saved)
    yearsUntilRetirement = years_until_retirement(totalSaved, goal)
    ageOfRetirement = age_of_retirement(age, yearsUntilRetirement)
    if ageOfRetirement == -1:
        return "You will not live to see your retirement"
    else:
        return "You will be able to retire at the age of " + str(ageOfRetirement)

def total_saved_per_year(salary, saved):
    return salary * (saved / 100) * 1.35

def years_until_retirement(totalSaved, goal):
    years = goal // totalSaved
    # round up if partial year
    if goal % totalSaved:
        years += 1
    return years

def age_of_retirement(age, yearsUntilRetirement):
    ageOfRetirement = age + yearsUntilRetirement
    if ageOfRetirement > 100:
        ageOfRetirement = -1
    return int(ageOfRetirement)