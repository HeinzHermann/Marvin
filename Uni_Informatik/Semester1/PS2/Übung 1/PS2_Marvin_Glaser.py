"""this module takes a date in one of two formats and converts it to 4 styles
4 styles includes german, UK and US style for date writing, + unix time stamp
module has 2 classes; ui class that interacts with user and tests for correct
input and dater class, that converts correct date to given output styles
"""

import datetime
import calendar



__author__ = "4424114: Marvin Glaser"
__credits__ = "no credits were given that day..."
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "marvin.glaser91@gmail.com"


class dater():
    """class is used for date conversion"""    
    
    def __init__(self):
        """constructs importand lists for rest of module"""
        
        self.months_german = ['Januar', 'Februar', 'März', 'April', 'Mai',
                              'Juni', 'Juli', 'August', 'September',
                              'Oktopber', 'November', 'Dezember'
                              ]
        
        self.months_english = ['January', 'February', 'March', 'April', 'May',
                               'June', 'July', 'August', 'September',
                               'October', 'November', 'December'
                               ]
        
        self.days_week_ger = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag',
                              'Freitag', 'Sonnabend', 'Sonnabend'
                              ]
        
        self.days_week_eng = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                              'Friday', 'Saturday', 'Sunday'
                              ]
        
    def dateconvert(self, date):
        """converts prepared and tested user date to 4 different output styles
        """
        
        #  convert parts of user date to integers for use with datetime funct.
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])

        #  prepare correct output for ger and UK days/month
        day_german = self.days_week_ger[datetime.date(year, month, day).weekday()]
        day_english = self.days_week_eng[datetime.date(year, month, day).weekday()]
        
        month_german = self.months_german[month - 1]
        month_english = self.months_english[month - 1]
        
        #  generate unix time stamp
        unix_raw = datetime.datetime(year, month, day, 12)
        unix_converted = calendar.timegm(unix_raw.utctimetuple())

        if int(day) < 10:
            #  add 0 to days with only one digit
            day = '0' + str(day)   
            
        if int(month) < 10:
            #  add 0 to month with only one digit
            month = '0' + str(month)
        
        
        #  construkt ger, UK and US dates
        german_date = day_german + ', ' + str(day) + '. ' + month_german 
        german_date = german_date + ' ' + str(year)
        
        british_date = day_english + ', ' + str(day) + ' ' + month_english
        british_date = british_date + ' ' + str(year)
        
        american_date = day_english + ', ' + str(month) + '/' + str(day)
        american_date = american_date + '/' + str(year)
        
        unix_date = unix_converted
        
        return_tuple = (german_date, british_date, american_date, unix_date)
        
        return(return_tuple)


class user_interface():
    """user interface class, bridge between user and data conversion"""
    def __init__(self):
        pass
    
    def gatekeeper(self, date):
        """tests user input for variaty of false inputs"""

        list_possible_days = ['01', '02', '03', '04', '05', '06', '07', '08',
                              '9', '10', '11', '12', '13', '14', '15', '16',
                              '17', '18', '19', '20', '21', '22', '23', '24',
                              '25', '26', '27', '28', '29', '30', '31'
                              ]
        
        #  checks for correct string length
        if len(date) > 8:
            print('\nSorry, but the string you entered was to long\nPlease '
                  'check your input and adjust it to your chosen format'
                  )
            return False
        elif len(date) < 8:
            print('\nSorry, but the string you entered was to short\nPlease '
                  'check your input and adjust it to your chosen format'
                  )
            return False
        
        try:
            if not date[0:4].s():
                print('\nSorry, but it appears that your input for YYYY '
                      'contianed other symbols than numbers\nPlease '
                      'check your input and adjust it to your chosen format'
                      )
                return False
            
            if not date[4:6].isnumeric():
                print('\nSorry, but it appears that your input for MM '
                      'contianed other symbols than numbers\nPlease '
                      'check your input and adjust it to your chosen format'
                      )
                return False
                
            if not date[6:].isnumeric():
                print('\nSorry, but it appears that your input for DD '
                      'contianed other symbols than numbers\nPlease '
                      'check your input and adjust it to your chosen format'
                      )
                return False
                
            #  check if year in correct range    
            if not 1801 <= int(date[0:4]) <= 2200:
                print('\nSorry, but it appears that your input year is outiside'
                      'the given range (1801 - 2200)\nPlease '
                      'check your input and adjust it to your chosen format'
                      )
                return False
            
            #  check if days are in a plausible range
            if date[6:] not in list_possible_days:
                print('\nSorry, but it appears that your input days are outiside'
                      'of the possible range (01 - 31)\nPlease '
                      'check your input and adjust it to your chosen format'
                      )
                return False
            
            #  check if month in correct range and days are in correct range
            if int(date[4:6]) in [1, 3, 5, 7, 8, 10, 12]:
                if int(date[6:]) not in range(1, 32):
                    print('\nSorry, but it appears that your input days are '
                          'outiside of the possible range of your input month'
                          '\nThe number of days in your chosen month range '
                          'between 01 and 31 days\nPlease check your input '
                          'and adjust either the number of days or the month'
                          )
                    return False
            elif int(date[4:6]) in [4, 6, 9, 11]:
                if int(date[6:]) not in range(1, 31):
                    print('\nSorry, but it appears that your input days are '
                          'outiside of the possible range of your input month'
                          '\nThe number of days in your chosen month range '
                          'between 01 and 30 days\nPlease check your input '
                          'and adjust either the number of days or the month'
                          )
                    return False
                
            elif int(date[4:6]) == 2:
                #  if february, check for leap year
                if int(date[:4]) // 4 != 0:
                    #  no leap year
                    if int(date[6:]) not in range(1, 29):
                        print('\nSorry, but it appears that your input days are '
                          'outiside of the possible range of your input month'
                          '\nThe number of days in your chosen month range '
                          'between 01 and 28 days\nPlease check your input '
                          'and adjust either the number of days or the month'
                          )
                        return False
                elif int(date[:4]) in [1900, 2100, 2200]:
                    #  no leap year
                    if int(date[6:]) not in range(1, 29):
                        print('\nSorry, but it appears that your input days are '
                          'outiside of the possible range of your input month'
                          '\nThe number of days in your chosen month range '
                          'between 01 and 28 days\nPlease check your input '
                          'and adjust either the number of days or the month'
                          )
                        return False
                elif int(date[:4]) == 2000:
                    #  leap year
                    if int(date[6:]) not in range(1, 30):
                        print('\nSorry, but it appears that your input days are '
                          'outiside of the possible range of your input month'
                          '\nThe number of days in your chosen month range '
                          'between 01 and 29 days (since this is a leap year!)'
                          '\nPlease check your input and adjust either the '
                          'number of days or the month'
                          )
                        return False
                else:
                    # leap year
                    if int(date[6:]) not in range(1, 30):
                        print('\nSorry, but it appears that your input days are '
                          'outiside of the possible range of your input month'
                          '\nThe number of days in your chosen month range '
                          'between 01 and 29 days (since this is a leap year!)'
                          '\nPlease check your input and adjust either the '
                          'number of days or the month'
                          )
                        return False
            
            #  month not in correct range
            else:
                print('\nSorry, but the month you have entered appears to be'
                      'outside of the possible range (01 - 12)\nPlease '
                      'check your input and adjust your input for month'
                      )
                return False
            
            #  entered date is in a valid format
            return True
                
        except:
            print('critical error')
            return False
    
    def date_prepare(self, date):
        """checks date in american style for input style related errors
        also converts input to dateconvert compatible format
        """
        
        #  checks for correct string length
        if len(date) > 10:
            print('\nSorry, but the string you entered was to long\nPlease '
                  'check your input and adjust it to your chosen format'
                  )
            return False
        elif len(date) < 10:
            print('\nSorry, but the string you entered was to short\nPlease '
                  'check your input and adjust it to your chosen format'
                  )
            return False
        
        #  checks for invalid special character
        if date[2] != '/' or date[5] != '/':
            print('\nSorry, but one or more of your special characters (/)'
                  'seem to be invalid\nPlease check your input for errors and'
                  'adjust it to your chosen format'
                  )
            return False
        
        self.new_date = date[6:] + date[:2] + date[3:5]
        return(True)
    
    def main_interface(self):
        """main function of the ui, handles interaction between
        ui and converter
        """
        #  loops until user input for date style is valid
        condition = True
        print('Dear user, this program lets you convert any date\n'
              'between 01. January 1801 and 31. Dezember 2200 to\n'
              'a german, a UK, a US date style and the Unix time\n stamp\n\n'
              'Please choose the format in which you would like to\n'
              'enter the date you would like the program to convert\n\n'
              'You can choose between:\nMethod 1 (type'
              ' \"M1\"; input format:   YYYYMMDD, I.e.:'
              '   20001231)\nMethod 2 (type \"M2\"; input'
              ' format: MM/DD/YYYY, I.e.: 12/31/2000)'
              )
        
        while condition:
            #  True till user inputs are valid
            user_input1 = input('Please enter your chosen method now: ')
        
            if user_input1 == 'M1':
                while True:
                    user_input2 = input('Please enter the date you would like'
                                        'to convert in the choosene format: '
                                        )
                    #  breaks while loops if user input is valid
                    if self.gatekeeper(user_input2):
                        condition = False
                        break
                
                convert = dater()
                
                #  converts user input to expected date versions
                for to_print in convert.dateconvert(user_input2):
                    print(to_print)
            
            elif user_input1 == 'M2':
                while True:
                    user_input2 = input('Please enter the date you would like'
                                        'to convert in the choosene format: '
                                        )
                    
                    #  breaks while loops if user input is valid
                    if self.date_prepare(user_input2):
                        if self.gatekeeper(self.new_date):
                            condition = False
                            break

                
                convert = dater()
                
                #  converts user input to expected date versions
                for to_print in convert.dateconvert(self.new_date):
                    print(to_print)
            
            else:
                print('\nWe are very sorry, but it seems'
                      ' like your input was invalid\nPlease type \"M1\"'
                      ' (for Method 1 YYYYMMDD) or\n\"M2\" (for Method 2 '
                      'MM/DD/YYYY)\n'
                      )
        


def main():
    """main function of the program"""
    runner = user_interface()
    runner.main_interface()

if __name__ == '__main__':
    main()
