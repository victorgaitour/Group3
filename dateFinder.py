import re

def get_potential_dates1(text):

    #dates in format 11/07/97
    dates = []
    exp = "\d\d?\/[01]?\d\/\d\d\d?\d?"

    for i in text:
        dates += re.findall(exp1, i)

    return dates



def get_potential_dates2(text);

    #dates in format November 7, 1997
    dates = []
    exp = "[A-Za-z]{3,} \d\d?,? \d{4}"

    for i in text:
         dates += re.findall(exp, i)

    return dates
