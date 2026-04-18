 #level 2.1 
import pandas as pd

df = pd.read_csv("Dataset1.csv")

print("=" * 40)
print("TASK 2.1 - STANDARDIZE TIME FIELDS")
print("=" * 40)

df['Arrival_time'] = pd.to_datetime(df['Arrival_time'],
                     format='%H:%M:%S', errors='coerce')
df['Departure_Time'] = pd.to_datetime(df['Departure_Time'],
                       format='%H:%M:%S', errors='coerce')

print("Arrival_time type  :", df['Arrival_time'].dtype)
print("Departure_Time type:", df['Departure_Time'].dtype)
print("\nSample Data:")
print(df[['Train_No', 'Station_Name',
          'Arrival_time', 'Departure_Time']].head(5))

#level 2.2

print("=" * 40)
print("TASK 2.2 - JOURNEY DURATION")
print("=" * 40)

first_stop = df.groupby('Train_No').first().reset_index()
last_stop = df.groupby('Train_No').last().reset_index()

journey = pd.DataFrame()
journey['Train_No'] = first_stop['Train_No']
journey['Start_Station'] = first_stop['Station_Name']
journey['End_Station'] = last_stop['Station_Name']
journey['Total_Distance_km'] = last_stop['Distance']

print(journey)
print("\nTotal Trains:", len(journey))

#level 2.3
print("=" * 40)
print("TASK 2.3 - CLASSIFY ROUTES")
print("=" * 40)

def classify_route(distance):
    if distance < 300:
        return 'short'
    elif distance < 800:
        return 'Medium'
    else:
        return 'Long'        
journey['Route_Type'] = journey['Total_Distance_km'].apply(classify_route)

print(journey[['Train_No', 'Total_Distance_km', 'Route_Type']])
print("\nRoute Type Summary:")
print(journey['Route_Type'].value_counts())

#level 2.4
print("=" * 40)
print("TASK 2.4 - STATION WISE TRAIN FREQUENCY")
print("=" * 40)

station_freq = df.groupby('Station_Name')['Train_No'].nunique().reset_index()
station_freq.columns = ['Station_Name', 'Train_Count']

station_freq = station_freq.sort_values('Train_Count', ascending=False)

print("Top 10 Stations with Most Trains:")
print("=" * 40)
print(station_freq.head(10))

print("\nBottom 10 Stations with Least Trains:")
print("=" * 40)
print(station_freq.tail(10))

print("\nTotal Stations:", len(station_freq))

#Task 2 Completed..