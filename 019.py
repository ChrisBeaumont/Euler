""" Just step through all of the days, instead of attempting any fancy
modulus math """

# number of days in given month, year
def days(month, year):
    d = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 2: return d[month]
    if year % 4 != 0: return 28
    if year % 100 != 0: return 29
    if year % 400 == 0: return 29
    return 28

dow = 0
result = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        for day in range(1, days(month, year) + 1):
            dow += 1
            is_first = day == 1
            is_sunday = dow % 7 == 0
            is_20th = year >= 1901
            if is_first and is_sunday and is_20th:
                result += 1

print result
            
