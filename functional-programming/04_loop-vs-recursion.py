"""
https://hackernoon.com/recursion-vs-looping-in-python-9261442f70a5
"""

# compounded interest using a loop

duration_years = 10
interest_rate = .06
compounded_per_year = 12 
principal_amount = 4000

def compound_interest_loop(principal, compounded, duration, rate):
    total_duration = compounded * duration
    for i in range(1, (total_duration+1)):
        principal = principal*(1+(rate/compounded))
    return principal
    
ci_loop = compound_interest_loop(principal_amount, compounded_per_year,duration_years,interest_rate)
print(f'Compound interest using a loop: {ci_loop}')

# compounded interest using recursion

def compound_interest_recursion(principal, compounded, duration, rate, compute_total_duration):
    if compute_total_duration:
        total_duration = compounded * duration
    else:
        total_duration = duration
    if duration == 0:
        return principal
    else:
        new_duration = total_duration - 1
        amount = principal*(1+(rate/compounded))
        return compound_interest_recursion(amount, compounded, new_duration, rate, False)

ci_recursion = compound_interest_recursion(principal_amount, compounded_per_year,duration_years,interest_rate, True)
print(f'Compound interest using recursion: {ci_recursion}')

assert(ci_loop == ci_recursion)
