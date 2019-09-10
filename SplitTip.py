# This module runs the Split the Tip

'''
Input a total dinner amount (ex. $55.40) and the number of guest to split the tab with. Add 15% gratuity to the total. 
The function should calculate the total tab (including tip) and as equally as possible distribute the cost of the entire 
meal between the number of provided guests. (e.g., splitTip ($15.16, 3) ==> guest1-$5.06, guest2-$5.05, guest3-$5.05). 
Whatever logic is used for uneven amounts should be deterministic and testable (all values rounded to cents - 2 decimal places). 
'''

def SplitTip(totalAmount, numberOfGuest):
    # First, verify that the data inputted is of the correct type
    if not isinstance(totalAmount,float):
        raise TypeError('Argument total amount must be passed as an float')
    if not isinstance(numberOfGuest,int):
        raise TypeError('Argument number of guests must be passed as an integer')

    # Next we test if the data makes sense given the domain
    # Make sure the total amount of the diner is more than 0 dollars
    # Make sure that there is at least one guest
    if totalAmount < 0:
        raise RuntimeError('Argument total amount must be greater than 0')
    if numberOfGuest < 1:
        raise RuntimeError('Argument number of guest must be greater than 1')

    totalWithTipInCents = calculate_total_with_tip(totalAmount,.15)
    leftOverCents = get_left_over_cents(totalWithTipInCents, numberOfGuest)
    distributedValuesWithoutLeftOverCents = get_distributed_values_without_left_over_cents(totalWithTipInCents - leftOverCents, numberOfGuest)
    distributedValues = get_distributed_values(distributedValuesWithoutLeftOverCents, leftOverCents)
    return make_return_string(distributedValues)

def calculate_total_with_tip(totalAmount, tipAmount):
    return round((totalAmount * (1 + tipAmount)),2) * 100

def get_left_over_cents(totalWithTip, numberOfGuest):
    return totalWithTip % numberOfGuest

def get_distributed_values_without_left_over_cents(totalWithOutLeftOverCents, numberOfGuest):
    pricePerPerson = totalWithOutLeftOverCents / numberOfGuest
    distributedValuesWithoutLeftOverCents = [float(pricePerPerson) / 100] * numberOfGuest
    return distributedValuesWithoutLeftOverCents

def get_distributed_values(distributedValuesWithoutLeftOverCents, leftOverCents):
    for i in range(int(leftOverCents)):
        distributedValuesWithoutLeftOverCents[i] = (distributedValuesWithoutLeftOverCents[i] + .01)
    return distributedValuesWithoutLeftOverCents

def make_return_string(distributedValues):
    guestList = []
    for i in range(len(distributedValues)):
        guestList.append("Guest")
        guestList.append(str(i + 1))
        guestList.append("-")
        guestList.append(str(distributedValues[i]))
        if i + 1 != len(distributedValues):
            guestList.append(", ")
    return ''.join(guestList)