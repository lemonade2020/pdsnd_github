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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Which city data do you want to explore? Choose from Chicago, New York City or Washington:\n').lower()

    while city not in ["chicago", "new york city", "washington"] :
        print("sorry! enter a valid city")
        city=input('Which city data do you want to explore? Choose from Chicago, New York City or Washington:')
        print(city)

# TO DO: get user input for month (all, january, february, ... , june)
    month=input('select desired month from January, February, March, April, May, June or all?\n').title()
    print("select:", month)
    while month not in ["January","February", "March", "April","May","June", "All"]:
        print("sorry! enter valid month")
        month=input('select desired month from January, February, March, April, May, June or all?\n').title()
    if month !='All':
        print("selected month is:", month)
    else:
        month =['January', 'Feburary', 'March', 'April', 'May', 'June']
        print("selected months are:", month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day=input('select desired day of the week or all: \n').title()
    if day !='All':
        print ("selected day of week is:", day)
    else:
        day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        print("you selected:", day)

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip

    # TO DO: display number of start stations

    # TO DO: display number of end stations

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


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

    i=0
    while True:
        raw_data=input('would you like to see next 5 rows of raw data? enter Yes or No:\n').lower()
        if raw_data!='yes':
            break

        else:
            print(df[i:i+5])
            i +=5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
