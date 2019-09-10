import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['Chicago','New York City','Washington']
    print('Valid City Names Are: {} \n'.format(city_list))
    
    valid_input = False
    while not valid_input:
        try:
            city = str(input('Please enter a city from the list of valid cities.\n'))
            print('\n')
            if city in city_list:
                valid_input = True
            else:
                raise ValueError
        except:
              print('"{}" is not a valid input. Please enter a city from the list of valid cities.\n'.format(city))

    # get user input for month (all, january, february, ... , june)
    #month = 'january'
    month_list = ['all','january', 'february', 'march', 'april', 'may', 'june']
    print('Months for which we have data are: {} \n'.format(month_list))
    
    valid_input = False
    while not valid_input:
        try:
            month = str(input('Please enter a month or all to select no filter. (all, january, february, ... , june)\n'))
            print('\n')
            if month in month_list:
                valid_input = True
            else:
                raise ValueError
        except:
              print('"{}" is not a valid mounth. Please enter a valid month or all.\n\n'.format(month))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    #day = 'Monday'
    day_list = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    print('Valid days are: {} \n'.format(day_list))
    
    valid_input = False
    while not valid_input:
        try:
            day = str(input('Please enter a day of the week or all to select no filter. (all, monday, tuesday, ... sunday)\n'))
            print('\n')
            if day in day_list:
                valid_input = True
            else:
                raise ValueError
        except:
              print('"{}" is not valid. Please enter a valid weekday or all.\n'.format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    #Make sure other city and Day are correct case
    city = city.lower()
    month = month.lower()
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        
        #Creat is month series to collect month indexes
        is_month = df['month'] == month
        
        # filter by month to create the new dataframe
        df = df[is_month]

    # filter by day of week if applicable
    if day != 'all':
        #Capitalize day parameter
        day = day.title()
        
        #Creat is day series to collect month indexes
        is_day = df['day_of_week'] == day
        
        # filter by day of week to create the new dataframe
        df = df[is_day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_m = df['month'].value_counts().idxmax()
    print('Month with the most use based on selected filter: {} \n'.format(common_m))
    
    # display the most common day of week
    common_wd = df['day_of_week'].value_counts().idxmax()
    print('Day of the week with the most use based on selected filter: {} \n'.format(common_wd))

    # display the most common start hour
    common_h = df['day_of_week'].value_counts().idxmax()
    print('Hour of the day with the most use based on selected filter: {} \n'.format(common_h))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
