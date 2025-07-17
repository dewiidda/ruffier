txt_index = "Your Rufier Index: "
txt_workheart = "Heart health: "
txt_nodata = '''
no data for this age'''
txt_res = [] 
txt_res.append('''low.
See a doctor immediately!''')
txt_res.append('''satisfactory.
See your doctor!''')
txt_res.append('''average.
It may be worth further examination by a doctor.''')
txt_res.append('''
above the average''')
txt_res.append('''
high''')

def ruffier_index(P1, P2, P3):
    ''' returns the index value for three heart rate indicators for comparison with the table'''
    return (4 * (P1+P2+P3) - 200) / 10

def neud_level(age):
    ''' variants with age less than 7 and adults must be processed separately,
     here we select the "bad" level only inside the table:
     at the age of 7 years "fail" is an index of 21, then every 2 years it decreases by 1.5 to a value of 15 at 15-16 years'''
    norm_age = (min(age, 15) - 7) // 2  # every 2 years, the difference from 7 years turns into a unit - up to 15 years
    result = 21 - norm_age * 1.5 # we multiply the difference by 1.5 every 2 years, this is how the levels are distributed in the table
    return result 
    
def ruffier_result(r_index, level):
    ''' the function gets the Rufier index and interprets it,
     returns readiness level: a number between 0 and 4
     (the higher the doneness level, the better).  '''
    if r_index >= level:
        return 0
    level = level - 4 # this will fail if we have already returned a "unsat" response
    if r_index >= level:
        return 1
    level = level - 5 # similarly, we get here if the level is at least "sat"
    if r_index >= level:
        return 2
    level = level - 5.5 # next level
    if r_index >= level:
        return 3
    return 4 # turned out to be here if the index is less than all intermediate levels, i.e. tested cool.

def test(P1, P2, P3, age):
    ''' this function can be used outside of the module for calculating the Rufier index.
     Returns ready-made texts, which remains to be drawn in the right place
     Uses the constants specified at the beginning of this module for texts.'''
    if age < 7:
        return (txt_index + "0", txt_nodata) # this secret is not for this test
    else:
        ruff_index = ruffier_index(P1, P2, P3) # calculation
        result = txt_res[ruffier_result(ruff_index, neud_level(age))] # interpretation, translation of the numerical level of training into text data
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res