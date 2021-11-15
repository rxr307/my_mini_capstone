from colorama import Fore, Style 
import requests
from datetime import date
import moment
import time
import calendar
from calendar_variables import calendar_days
from calendar_variables import holiday_dict

def lifespan_main(year, month, day):
    now = moment.now().format("YYYY-M-D")
    now = now.replace('-', ' ')
    now = now.split(' ')
    int_list = []
    for number in now:
        number = int(number)
        int_list.append(number)

    user_birthday_list = []
    user_birthday_list.append(year)
    user_birthday_list.append(month)
    user_birthday_list.append(day)
    current_date = date(int_list[0], int_list[1], int_list[2])
    birth_date = date(user_birthday_list[0], user_birthday_list[1], user_birthday_list[2])
    how_long1 = current_date - birth_date
    return how_long1.days

def time_alive_calc(days_alive, year, month, day):
        years_alive = int(days_alive / 365)
        months_alive = years_alive * 12
        days_alive = days_alive
        hours_alive = days_alive * 24
        minutes_alive = hours_alive * 60
        seconds_alive = minutes_alive * 60
        alive_figures_dict = {'years_key': ("{:,}".format(years_alive)), 'months_key': ("{:,}".format(months_alive)), 'days_key': ("{:,}".format(days_alive)), 'hours_key': ("{:,}".format(hours_alive)),'minutes_key': ("{:,}".format(minutes_alive)),'seconds_key': ("{:,}".format(seconds_alive))}
        return alive_figures_dict

def time_remaining_calc(total_years_alive, year, month, day):
    years_remaining = 79 - total_years_alive
    months_remaining = years_remaining * 12
    days_remaining = months_remaining * 30
    hours_remaining = days_remaining * 24
    minutes_remaining = hours_remaining * 60
    seconds_remaining = minutes_remaining * 60
    remaining_figures_dict = {'years2_key': ("{:,}".format(years_remaining)), 'months2_key': ("{:,}".format(months_remaining)), 'days2_key': ("{:,}".format(days_remaining)), 'hours2_key': ("{:,}".format(hours_remaining)),'minutes2_key': ("{:,}".format(minutes_remaining)),'seconds2_key': ("{:,}".format(seconds_remaining))}
    return remaining_figures_dict

def holiday_calculator(holiday):

    now = moment.now().format("YYYY-M-D")
    now = now.replace('-', ' ')
    now = now.split(' ')
    int_list = []
    for number in now:
        number = int(number)
        int_list.append(number)
    date_chosen = holiday_dict[holiday]
    current_date = date(int_list[0], int_list[1], int_list[2])
    holiday_date = date(date_chosen[0], date_chosen[1], date_chosen[2])
    how_long2 = holiday_date - current_date
    return how_long2.days

def weight_loss_caclcuator(current_weight, goal_weight, total_months):
    total_weight_loss = current_weight - goal_weight
    loss_per_month = total_weight_loss / total_months
    return loss_per_month

def weight_loss_print(total_months, loss_per_month):
    print(f'''
You will need to lose the following amount of weight to reach your goal weight in {total_months} months:
~{round(loss_per_month, 2)} lbs per month
~{round(loss_per_month/30, 2)} lbs per day
~{round(loss_per_month/730, 2)} lbs per hour
''')

def new_weight_loss_print(new_total_months, loss_per_month):
    print(Fore.GREEN + f'''
You will need to lose the following amount of weight to reach your goal weight in {new_total_months} months:
~{round(loss_per_month, 2)} lbs per month
~{round(loss_per_month/30, 2)} lbs per day
~{round(loss_per_month/730, 2)} lbs per hour
''')            

def savings_return(savings_account, years):
    interest = savings_account * years * .006
    savings_account = round((interest + savings_account), 2)
    savings_account = "{:,}".format(savings_account)
    return savings_account
def savings_return_int(savings_account, years):
    interest = savings_account * years * .006
    savings_account = round((interest + savings_account), 2)
    return savings_account

def retirement_calculator(yearly_contribution, years, four_one_k, avg_annual_return = 1.07):
    # this formuala is not my own and was located at: https://gist.github.com/jiaaro/6780635
    total_four_one_k = four_one_k * (avg_annual_return ** years)
    while years > 0:
        years -= 1
        total_four_one_k += yearly_contribution * (avg_annual_return ** years)
    total_four_one_k = round(total_four_one_k, 2)
    total_four_one_k = "{:,}".format(total_four_one_k)
    return total_four_one_k
def retirement_calculator_int(yearly_contribution, years, four_one_k, avg_annual_return = 1.07):
    total_four_one_k = four_one_k * (avg_annual_return ** years)
    while years > 0:
        years -= 1
        total_four_one_k += yearly_contribution * (avg_annual_return ** years)
    total_four_one_k = round(total_four_one_k, 2)
    return total_four_one_k

def home_return(home_value, years):  
    home_value = int(home_value)
    home_value = home_value * (1.036 ** years)
    home_value = round(home_value, 2)
    home_value = "{:,}".format(home_value)
    return home_value
def home_return_int(home_value, years):  
    home_value = int(home_value)
    home_value = home_value * (1.036 ** years)
    home_value = round(home_value, 2)
    return home_value

def misc_return(miscellaneous, misc_interest, years): 
    misc_interest = int(misc_interest)    
    misc_interest = misc_interest / 100 
    miscellaneous = int(miscellaneous * misc_interest)
    miscellaneous = round(miscellaneous * years, 2)
    miscellaneous = "{:,}".format(miscellaneous)
    return miscellaneous
def misc_return_int(miscellaneous, misc_interest, years): 
    misc_interest = int(misc_interest)    
    misc_interest = misc_interest / 100 
    miscellaneous = int(miscellaneous * misc_interest)
    miscellaneous = round(miscellaneous * years, 2)
    return miscellaneous

def what_month_finder(what_month):
    string_to_integer = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    int_value = string_to_integer[what_month]
    return int_value

def calendar_printer(what_year, multiple_months, calendar_days, days_list, what_day):
    string_to_integer = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    print(f"\n{what_year} calendar:")
    time.sleep(1)
    x = 1
    for months in multiple_months:
        string_to_integer = what_month_finder(months)
        print('\n')
        print(calendar.month(what_year, string_to_integer, w=0, l=0))
        print(Fore.YELLOW + f'List of events for {months}:')
        print(Fore.WHITE + '---------------------------------------')
        for x in range(1, 32):
            if calendar_days[months][str(x)] != " ":
                if x in days_list:
                    what_day = x
                print(Fore.WHITE + f'{what_day}.) {calendar_days[months][str(x)]}')
                x =+ 1

def month_calendar_printer(what_year, list_of_months, calendar_days, days_list, what_day):
    string_to_integer = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    print(f"\nYou made the following updates to your {what_year} calendar:")
    time.sleep(1)
    x = 1
    for months in list_of_months:
        string_to_integer = what_month_finder(months)
        print('\n')
        print(calendar.month(what_year, string_to_integer, w=0, l=0))
        print(Fore.YELLOW + f'List of events for {months}:')
        print(Fore.WHITE + '---------------------------------------')
        for x in range(1, 32):
            if calendar_days[months][str(x)] != " ":
                if x in days_list:
                    what_day = x
                print(Fore.WHITE + f'{what_day}.) {calendar_days[months][str(x)]}')
                x =+ 1


def time_alive_print(alive_figures_dict, total_years_alive, remaining_figures_dict):
    print('\nYou have been alive for:')
    time.sleep(2)
    print(Fore.RED + f"\n{alive_figures_dict['years_key']} years! (you probably know that already)")
    time.sleep(2)
    print(Fore.YELLOW + f"{alive_figures_dict['months_key']} months!")
    time.sleep(2)
    print(Fore.RED + f"{alive_figures_dict['days_key']} days!") 
    time.sleep(2)
    print(Fore.YELLOW + f"{alive_figures_dict['hours_key']} hours!")
    time.sleep(2)
    print(Fore.RED + f"{alive_figures_dict['minutes_key']} minutes!") 
    time.sleep(2)
    print(Fore.YELLOW + f"{alive_figures_dict['seconds_key']} seconds!")
    time.sleep(3)
    percentage = round((total_years_alive / 79)*100, 2)
    print(Fore.WHITE + f'''
--The average lifepsan in the USA is 79 years--
--Compared to the AVERAGE, you have lived {percentage} % of your life-- 
--And your average remaining lifespan is:''')
    time.sleep(7)
    print(Fore.RED + f"\n{remaining_figures_dict['years2_key']} years!")
    time.sleep(2)
    print(Fore.YELLOW + f"{remaining_figures_dict['months2_key']} months!")
    time.sleep(2)
    print(Fore.RED + f"{remaining_figures_dict['days2_key']} days!") 
    time.sleep(2)
    print(Fore.YELLOW + f"{remaining_figures_dict['hours2_key']} hours!")
    time.sleep(2)
    print(Fore.RED + f"{remaining_figures_dict['minutes2_key']} minutes!") 
    time.sleep(2)
    print(Fore.YELLOW + f"{remaining_figures_dict['seconds2_key']} seconds!")
    print(Fore.WHITE + f"\nMake every one of your {remaining_figures_dict['seconds2_key']} seconds count! \U0001F609 \U0001F609")

def print_current_portfolio(four_one_k, savings_account, home_value, miscellaneous):
    current_portfolio = round((four_one_k + savings_account + home_value + miscellaneous), 2)
    current_portfolio_string = ("{:,}".format(current_portfolio))
    four_one_k_string = ("{:,}".format(four_one_k))
    savings_account_string = ("{:,}".format(savings_account))
    home_value_string = ("{:,}".format(home_value))
    miscellaneous_string = ("{:,}".format(miscellaneous))
    print(Fore.YELLOW + f"Your current portfolio is valued at ${current_portfolio_string} and is comprised of:")
    print(Fore.WHITE + f'''
${four_one_k_string} in 401k ({round((four_one_k / current_portfolio) * 100, 2)} % of current portfolio)
${savings_account_string} in savings ({round((savings_account / current_portfolio) * 100, 2)} % of current portfolio)
${home_value_string} in home value ({round((home_value / current_portfolio) * 100, 2)} % of current portfolio)
${miscellaneous_string} in miscellaneous investments ({round((miscellaneous / current_portfolio) * 100, 2)} % of current portfolio)
''')
def print_future_portfolio(savings_account, years, miscellaneous, misc_interest, home_value, yearly_contribution, four_one_k):
    savings_return_future = savings_return(savings_account, years)
    misc_return_future = misc_return(miscellaneous, misc_interest, years)
    home_return_future = home_return(home_value, years)
    four_one_k_future = retirement_calculator(yearly_contribution, years, four_one_k)
    savings_return_future_int = savings_return_int(savings_account, years)
    misc_return_future_int = misc_return_int(miscellaneous, misc_interest, years)
    home_return_future_int = home_return_int(home_value, years)
    four_one_k_future_int = retirement_calculator_int(yearly_contribution, years, four_one_k)
    total_future_portfolio = round((savings_return_future_int + misc_return_future_int + home_return_future_int + four_one_k_future_int), 2)
    total_future_portfolio_str = str(total_future_portfolio)
    total_future_portfolio_str = ("{:,}".format(total_future_portfolio))
    print(Fore.YELLOW + f"Your expected future portfolio (in {years} years from now) is valued at ${total_future_portfolio_str} and is comprised of:")
    print(Fore.WHITE + f'''
${four_one_k_future} in 401k ({round((four_one_k_future_int / total_future_portfolio) * 100, 2)} % of future portfolio)
${savings_return_future} in savings ({round((savings_return_future_int / total_future_portfolio) * 100, 2)} % of future portfolio)
${home_return_future} in home value ({round((home_return_future_int / total_future_portfolio) * 100, 2)} % of future portfolio)
${misc_return_future } in miscellaneous investments ({round((misc_return_future_int / total_future_portfolio) * 100, 2)} % of future portfolio)
''')

user_entry = ''

while user_entry != '8':
    user_entry = input(Fore.WHITE + '''

\U0001F570  \U0001F570  \U0001F570  Welcome to the TIME MACHINE \U0001F570  \U0001F570  \U0001F570  

Please enter a number to access a function or 'exit' to exit the application:

1 - The Calendar               2 - How many days until... 

3 - Weight Loss Calculator     4 - Future Net Worth 

5 - Time Alive                 6 - Random Time Facts
                  --exit--           
\n> ''')

    # user entry 1 -----------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------

    if user_entry == '1':
        try_again1 = 'yes'
        while try_again1 == 'yes':
            list_of_months = []
            multiple_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            days_list = []
            what_month = ''
            print(Fore.YELLOW + "Welcome to your calendar \U0001F4C5\n")
            add_event = input(Fore.WHITE + "Would you like to make any changes?\n> ")
            if add_event == 'no':
                break
            what_year = int(input('\nWhat year?\n> '))
            if add_event == 'yes':
                while add_event == 'yes':
                    what_month = (input("\nMonth?\n> ")).capitalize()
                    list_of_months.append(what_month)
                    what_day = int(input("\nDay?\n> "))
                    days_list.append(what_day)
                    event = (input("\nDescribe event:\n> "))
                    calendar_days[what_month][str(what_day)] = event
                    add_another_event = input('\nWould you like to add another event?\n> ')
                    if add_another_event == 'yes':
                        continue
                    else:
                        break
            month_or_year = input("\nEnter '1' to see calendar updates. Enter '2' to see full year calendar:\n> ")
            if month_or_year == '1':
                month_calendar_printer(what_year, list_of_months, calendar_days, days_list, what_day)
            elif month_or_year == '2':
                calendar_printer(what_year, multiple_months, calendar_days, days_list, what_day)
            try_again1 = 'no'
        
# user entry 2 ----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
    elif user_entry == '2':
        try_again2 = 'yes'
        holiday_list = ['Christmas','Halloween','Independence Day', 'New Years Eve', 'Thanksgiving','Easter','Mothers Day','Fathers Day','Memorial Day','Mlk Day','Labor Day','Veterans Day']
        while try_again2 == 'yes':
            print(Fore.WHITE + "Calculate how many days until your favorite holiday!\n")
            holiday = input(Fore.WHITE + 'Please enter a major holiday:\n> ').title()
            if holiday not in holiday_list:
                print('ERROR: Please enter a major holiday only')
                continue
            number_of_days = holiday_calculator(holiday)
            print(Fore.GREEN + f'\nThere are {number_of_days} days until {holiday}')
            try_again2 = input(Fore.WHITE + '\nWould you like to try again, yes or no?\n> ')

    # user entry 3 -------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------
    elif user_entry == '3':
        try_again3 = 'yes'
        while try_again3 == 'yes':
            print(Fore.WHITE + "Weight Loss Calculator \n")
            current_weight = int(input("What is your current weight?\n> "))
            goal_weight = int(input("What is your goal weight?\n> "))
            total_months = int(input("Enter how many months you would like to reach your goal weight?\n> "))
            loss_per_month = weight_loss_caclcuator(current_weight, goal_weight, total_months)
            weight_loss_print(total_months, loss_per_month)

            pos_neg = (input("Enter '+' to extend or '-' to reduce the time to reach your goal:\n> "))
            if pos_neg == '+':
                new_total_months = total_months + int(input('How many months do you want to add?\n> '))
                loss_per_month = weight_loss_caclcuator(current_weight, goal_weight, new_total_months)
                new_weight_loss_print(new_total_months, loss_per_month)

            elif pos_neg == '-':
                new_total_months = total_months - int(input('How many months do you want to remove?\n> '))
                loss_per_month = weight_loss_caclcuator(current_weight, goal_weight, new_total_months)
                new_weight_loss_print(new_total_months, loss_per_month)

            try_again3 = input('Would you like to try again, yes or no?\n> ')

  # user entry 4 ------------------------------------------------------------------------------------------------------------------
  #--------------------------------------------------------------------------------------------------------------------------------

    elif user_entry == '4':
        try_again4 = 'yes'
        while try_again4 == 'yes':
            # current portfolio input --------------------------------------
            print(Fore.WHITE + '\nWelcome to the Future Net Worth Calculator \U0001F4B0 \U0001F4B0 \U0001F4B0 \n')
            print(Fore.YELLOW + 'First we will ask some questions about your investments\n') 
            four_one_k = int(input(Fore.WHITE + "Enter current amount invested in 401K or 0 if none:\n> "))
            savings_account = int(input("Enter current amount in savings account or 0 if none:\n> "))
            home_worth = int(input("Enter current value of home or 0 if you do not own a home:\n> "))
            mortgage = int(input("Enter current amount owed on mortgage or 0 if you own home outright:\n> "))
            home_value = home_worth - mortgage
            miscellaneous = int(input("Enter amount of miscellaneous investments (cryptocurrency, for example):\n> "))
            print_current_portfolio(four_one_k, savings_account, home_value, miscellaneous)

            # future portfolio input ----------------------------------------
            print(Fore.YELLOW + '\nNow a few more questions to determine the potential future value of your portfolio')
            current_age = int(input(Fore.WHITE + "Current age:\n> "))
            retirement_age = int(input("Retirement age:\n> "))
            years = retirement_age - current_age
            salary = int(input("Annual salary:\n> "))
            contribution_rate = int(input("Salary contribution rate to 401K in %:\n> "))
            yearly_contribution = salary * (contribution_rate / 100)
            misc_interest = input("Anticipated % return on misc investments (others based on national averages):\n> ")
            if misc_interest == '':
                misc_interest = 0
            print_future_portfolio(savings_account, years, miscellaneous, misc_interest, home_value, yearly_contribution, four_one_k)
            
            try_again4 = input(Fore.WHITE + '\nWould you like to try again, yes or no?\n> ')

    # user entry 5 ------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------
    elif user_entry == '5':
        try_again5 = 'yes'
        while try_again5 == 'yes':
            print(Fore.WHITE + "Answer the following questions to see interesting tidbits regarding your life span:\n")
            year = int(input('What year were you born?\n> '))
            month = int(input('What month were you born (please enter number for month)?\n> '))
            day = int(input('What day were you born?\n> '))
            days_alive = int(lifespan_main(year, month, day))
            alive_figures_dict = (time_alive_calc(days_alive, year, month, day))
            total_years_alive = int(round((days_alive / 365), 0))
            years_alive = alive_figures_dict['years_key']
            remaining_figures_dict = time_remaining_calc(total_years_alive, year, month, day)
            time_alive_print(alive_figures_dict, total_years_alive, remaining_figures_dict)
            try_again5 = input(Fore.WHITE + '\nWould you like to try again, yes or no?\n> ')

    # user entry 6 -------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------
    
    elif user_entry == '6':
        try_again6 = 'yes'
        while try_again6 == 'yes':
            print(Fore.YELLOW + 'Random Time Facts')
            print(Fore.WHITE + 'Please enter a month and a day (numbers only) to receive a random time fact about that day in history!')
            month = input('\nMonth:\n> ')
            day = input('Day:\n> ')
            request_string = 'http://numbersapi.com/' + month + '/' + day + '/date'
            response = requests.get(request_string, headers = {'Content-Type': 'application/json'})
            data = response.json()  
            print(data['text'])
            try_again6 = input(Fore.WHITE + '\nWould you like to try again, yes or no?\n> ')

    elif user_entry == 'exit':
        break 
















