__author__ = "4424114: Marvin Glaser"

# EPR1
# Exerciise 1, 1.3
# Bald ist Weihnachten
"""
strategy for the problem:
calculate how many days have passed since the beginning of the year
substract the days that have passed from the day of the year christmas is on (day 359)
code exeptions for days after christmas and christmas itself
"""

USER_INPUT = str(input("--> "))

day = int(USER_INPUT[0 : 2])
month = int(USER_INPUT[2 : 4])

"""
define user input as string for easy sliceing
slice days and months from input string and convert to integer
ignore year, since leap years not included in problem
"""

counter = 1
passed_time_month = 0

while counter < month:

    if counter <= 7:
        """
        month 7 and 8 both have 31 days. This reverses days added per month
        for eaven and uneven month
        exeption needs to be coded for february (only 28 month)
        """
        if counter == 2:
            passed_time_month += 28
            counter += 1
        else:
            if counter % 2 == 0:
                passed_time_month += 30
                counter += 1
            else:
                passed_time_month += 31
                counter += 1
    else:
        if counter % 2 == 0:
            passed_time_month += 31
            counter += 1
        else:
            passed_time_month += 30
            counter += 1

"""
Days so far only calculated for fully past month
upcoming step adds past days in current month
"""

time_passed_total = passed_time_month + day

days_till_christmas = 359 - time_passed_total

"""
check if christmas is coming (this year), has already passed
or if the input date is christmas day
"""

if days_till_christmas < 0:
    print(365 + days_till_christmas)
else:
    if days_till_christmas == 0:
        print(0)
    else:
        print(days_till_christmas)