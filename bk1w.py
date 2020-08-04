import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city = ' '

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
    while month not in ["January","February", "March", "April","May","June", "All"]:
        print("sorry! enter valid month")
        month=input('select desired month from January, February, March, April, May, June or all?\n').title()
    if month !='All':
        print("selected month is:", month)



        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('select desired day of the week or all: \n').title()
    while day not in ["Sunday","Monday", "Tuesday", "Wednesday","Thursday","Friday", "Saturday", "All"]:
        print("sorry! enter valid day of week")
        day=input('select desired day of the week or all: \n').title()

    if day !='All':
        print( "selected day is:", day)


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
    print ("summary of the available data for:", city)
    df.info()

    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month_name()
    df['week_day']=df['Start Time'].dt.day_name()
    df['start_hour']=df['Start Time'].dt.hour
    df['end_hour']=df['End Time'].dt.hour
    column_names=df.columns

    while True:
        if month != 'All':
            df=df[df['month']==month]


        return df

        if day !='All':
            df = df[df['week_day'] == day]

        return df

        break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print("month with most frequent travels:", common_month)
    count=df[df['month']==common_month].count().max()
    print("count", count)

    # TO DO: display the most common day of week
    common_day=df['week_day'].mode()[0]
    print ("week day with most frequent travels:", common_day)
    count_common_day=df[df['week_day']==common_day].count().max()
    print("count", count_common_day)



    # TO DO: display the most common start hour
    common_start_hour=df['start_hour'].mode()[0]
    print ("the most common start hour is:",common_start_hour)
    count_common_start_hour=df[df['start_hour']==common_start_hour].count().max()
    print("count", count_common_start_hour)

    common_end_hour=df['end_hour'].mode()[0]
    print ("the most common end hour is:", common_end_hour)
    count_common_end_hour=df[df['end_hour']==common_end_hour].count().max()
    print("count", count_common_end_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display number of start stations
    unique_start_stations=df['Start Station'].unique().size
    print("number of start stations are:", unique_start_stations)

    # TO DO: display number of end stations
    unique_end_stations=df['End Station'].unique().size
    print("number of end stations are:", unique_end_stations)


    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print ("the most frequent used start station:", common_start_station)
    count_common_start_sta=df[df['Start Station']==common_start_station].count().max()
    print("count", count_common_start_sta)


    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("the most frequent used end station:", common_end_station)
    count_common_end_sta=df[df['End Station']==common_end_station].count().max()
    print("count", count_common_end_sta)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    print('The most frequent combined start station and end station is\n {}'.format((df['combination'].mode()[0])))
    freq_comb=df['combination'].mode()[0]
    count_freq_comb=df[df['combination']==freq_comb].count().max()
    print("count", count_freq_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time in seconds:", total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time=int(df['Trip Duration'].mean())
    print("average travel time in seconds:", avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df.groupby('User Type').size()
    print(user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count=df.groupby('Gender').size()
        print(gender_count)

    else:
        print ("washington does not have gender data")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest_year= int(df['Birth Year'].min())
        youngest_year=int(df['Birth Year'].max())
        most_common_birth_year=int(df['Birth Year'].mode())
        print("oldest:", oldest_year)
        print ("youngest:", youngest_year)
        print("most common birth year:",most_common_birth_year)
        count_common_by=df[df['Birth Year']==most_common_birth_year].count().max()
        print("count", count_common_by)

    else:
        print ("washington does not have birth year data")


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
