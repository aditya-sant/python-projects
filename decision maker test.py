"""
>>> job(12, 1)
'Accept'

>>>job(1, 9)
'Decline'

>>> job(2, 5)
'Negotiate'

>>> job(12, 8)
'Negotiate'

"""
def job(duration, difficulty):

    hard = 7 #out of 10
    short = 3 # months

    if difficulty >= hard and duration <= short:
        return 'Decline'
    elif difficulty < hard and duration > short:
        return 'Accept'
    else:
        return 'Negotiate'
    
from doctest import testmod
print(testmod())
