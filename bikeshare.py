import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = [ 'january', 'february', 'march', 'april','may', 'june']
month = ''   
days= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
day = ''
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
    while True:
        try:
            city_selection = input('To view the available bikeshare data, kindly type:\n The letter(c) for Chicago\n The letter (n) for New York City\n The letter (w) for Washington\n ').lower()
            if city_selection in {'c', 'n', 'w'}:
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('That\'s invalid input.')

     
    if city_selection == "c":
        city ='chicago'
    elif city_selection == "n":
        city = 'new york city'
    elif city_selection == "w":
        city = 'washington'


    # TO DO: get user input for month (all, january, february, ... , june)
    months = [ 'january', 'february', 'march', 'april','may', 'june']
    day= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 
    while True: 
        try:
            time_frame= input("Would you like to filter by month, day, both or none?\n").lower()
            if time_frame in ['month','day','both','none']:
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('That\'s invalid input.')
    if time_frame == 'none':
         print('\nFiltering for {} for the 6 months period\n\n'.format(city.title()))
         month = 'all'
         day = 'all'
    elif time_frame == 'both':
        while True:
          try:
            month_selection = input("Wich month? January, February, March, April, May, or June\n").lower()
            if month_selection in ['january', 'february', 'march', 'april', 'may', 'june']:
                            month = month_selection
                            break
          except KeyboardInterrupt:
                print('\nNO Input Taken!')
          else:
            print('Invalid month choice!!')
        while True:
          try:
            day_selection = input("Choose a day from Monday to Sunday\n").lower()
            if day_selection in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                            day = day_selection
                            break
          except KeyboardInterrupt:
             print('\nNO Input Taken!')
          else:
             print('Invalid day choice!!')
                            
    elif time_frame == 'month':
          while True:
            try:
             month_selection = input("Wich month? January, February, March, April, May, or June\n").lower()
             if month_selection in ['january', 'february', 'march', 'april', 'may', 'june']:
                            month = month_selection
                            day = 'all'
                            break
            except KeyboardInterrupt:
                print('\nNO Input Taken!')
            else:
                print('Invalid month choice!!')
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif time_frame == 'day':
        while True:
           try:
            day_selection = input("Choose a day from Monday to Sunday\n").lower()
            if day_selection in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                            day = day_selection
                            month = 'all'
                            break
           except KeyboardInterrupt:
                print('\nNO Input Taken!')
           else:
                print('Invalid day choice!!')
                            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)
    return (city, month, day)
    

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
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n') 
    start_time = time.time()    
    # TO DO: display the most common month
    most_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    most_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print('Most common month is:', most_month)
    print('Most common Day is:', most_day)
    print('Most common start hour is:', most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode().values[0]
    print('\nMost Commonly used start station:', most_start_station)
    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode().values[0]
    print('\nMost Commonly used end station:', most_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['End Station','Start Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', most_start_station, " & ", most_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
      
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time/86400, " Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time, "minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:\n", user_types)

    # TO DO: Display counts of gender
    
    while True:
        try:
            gender_type = df['Gender'].value_counts()
            print('\nGender Types:\n', gender_type)

    # TO DO: Display earliest, most recent, and most common year of birth
            earliest_year = df['Birth Year'].min()
            most_recent_year = df['Birth Day'].max
            most_common_year = df['Birth Year'].value_counts().idxmax()
            print('\nEarliest Year:', earliest_year)
            print('\nMost Recent Year:', most_recent_year)  
            print('\nMost Common Year:', most_common_year)
            break 
        except KeyError:
            print("This data is not available for Washington") 
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def display_raw_data(city):
   print('\nRaw data is available to check... \n')
   display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
   while display_raw not in ('yes', 'no'):
       print('That\'s invalid input, please enter your selection again')
       display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
   
   while display_raw == 'yes':
       try:
           for chunk in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
               print(chunk)
               display_raw = input('To View the availbale raw in chuncks of 5 rows type: Yes\n').lower()
               if display_raw != 'yes':
                   print('Thank You')
                   break
               break 

       except KeyboardInterrupt:
           print('Thank you.')
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()