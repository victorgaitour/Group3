import re


months = {'january': 1, 'febuary': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
months_abb= {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "june": 6, "july": 7, "aug": 8, "sept": 9, "oct": 10, "nov": 11, "dec": 12}

txt = "dhgkgdhdgh 2/7/1997 wejthjth Febuary 5 1998 2/5/1998"

def get_potential_dates1(text):

    #dates in format 11/07/97
    dates = []
    exp = "\d\d?\s?\/\s?[01]?\d\s?\/\s?\d{4}"

    dates += re.findall(exp,text)
    return dates



def get_potential_dates2(text):

    #dates in format November 7, 1997
    dates = []
    exp = "[A-Za-z]{3,}.? \d\d?,? \d{4}"

    dates += re.findall(exp, text)

    return dates

def check_dates1(potential_dates):
    checked_dates = []

    for i in potential_dates:
        month = i.split("/")[0]
        day = i.split("/")[1]
        year = i.split("/")[2]

        monthT = int(month) > 0 and int(month) < 13
        dayT = int(day) > 0 and int(day) < 32
        yearT = int(year) > 0 and int(year) < 2015


        if monthT == True and dayT == True and yearT == True:
            checked_dates.append(i);
        

    return checked_dates

def check_dates2(potential_dates):
    checked_dates = []
    for i in potential_dates:
        month = i.split(" ")[0].lower()
        day = i.split(" ")[1]
        year = i.split(" ")[2]

        if month[-1:] == ".":
            month = month[:-1]

        if day[-1:] == ",":
            day = day[:-1]
            
        monthN = 0
        if month in months:
            monthN = months[month]
        if month in months_abb:
            monthN = months_abb[month]

        if monthN != 0:
            monthT = True
        else:
            monthT = False

        dayT = int(day) > 0 and int(day) < 32
        yearT = int(year) > 0 and int(year) < 2015

        if monthT == True and dayT == True and yearT == True:
            checked_dates.append( str(monthN) + "/" + str(day) + "/" + str(year))

        return checked_dates


def combine_data( checked1, checked2):
    dates = {}
    for date in checked1:
        if date in dates:
            dates[date] += 1
        else:
            dates[date] = 1

    for date in checked2:
        if date in dates:
            dates[date] += 1
        else:
            dates[date] = 1
    return dates

    

        



print( combine_data( check_dates1(get_potential_dates1(txt)), check_dates2(get_potential_dates2(txt))) )
