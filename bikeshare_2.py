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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york', 'washington']
    while True :
        city = input('Please choose a city you like to filter on. ').lower()
        if city not in cities :
            print('Invalid city, try again.')
        else :
            break
    

    # get user input for month (all, january, february, ... , june)
    months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True :
        month = input('Please choose a month you like to filter on or you can chosse all. ').lower()
        if month not in months_list :
            print('Invalid month, try again.')
        else :
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    ddays_list = ['saturday','sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday','all' ]
    while True :
        days_list = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        day = input('Please chosse a day you like to filter on or you can chosse all. ').lower()
        if day not in days_list :
            print('Invalid day, try again.')
        else :
            break
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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A').str.lower() 

    if month != 'all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.lower()]

    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_popular_month = df['month'].mode()[0]
    print('Most popular month is : ', most_popular_month)

    # display the most common day of week

    most_popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most popular day of the week is : ', most_popular_day_of_week)

    # display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()[0]
    print('Most popualr hour is : ',most_popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station is : ', most_popular_start_station)

    # display most commonly used end station

    most_popular_end_station = df['Start Station'].mode()[0]
    print('Most popular end station is : ',most_popular_end_station)

    # display most frequent combination of start station and end station trip

    df['Full Trip'] = df['Start Station'] + ' ' + df['Start Station']
    most_popular_full_trip = df['Full Trip'].mode()[0]
    print('Most popular full trip is : ',most_popular_full_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = sum(df['Trip Duration'])

    print('Total trip travel time is : ', total_travel_time)

    # display mean travel time

    mean_travel_time  = np.mean(df['Trip Duration'])
    print('Mean travel time is :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    counts_of_user_types = df['User Type'].value_counts()
    print('Counts of user types are : ',counts_of_user_types)


    # Display counts of gender
    
    try :
        counts_of_gender = df['Gender'].value_counts()
        print('Counts of genders are : ',counts_of_gender)
    except :
        print('Gender column is not avilable.')
         

    # Display earliest, most recent, and most common year of birth

    try :
        earliest_year = min(df['Birth Year'])
        print('Earliest birth year is : ', earliest_year)

        most_recent_year = max(df['Birth Year'])
        print('Most recent birth year is : ', most_recent_year)

        most_common_year = df['Birth Year'].mode([0])
        print('Mots common birth year is : ', most_common_year)


    except:
        print('Birth year column is not avilable.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city, month, day,df):
    counter = 0
    while True:
        q1 = input('Would you like to see 5 rows of the data ? ')
        if q1 == 'yes' :
            statment = df[counter:counter + 5]
            print(statment)
            counter += 5
        else :
            print("See you soon ^_^")
            break
                



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city, month, day,df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
