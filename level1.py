
# level 1.1
import pandas as pd

df = pd.read_csv("Dataset1.csv")

print("=" * 40)
print(" Task 1.1 DATASET OVERVIEW")
print("=" * 40)
print("Total Records (Rows) :", df.shape[0])
print("Total Attributes (Columns) :", df.shape[1])
print("\nColumn Names:")
for col in df.columns:
    print("  -", col)
print("\nFirst 5 rows of data:")
print(df.head())
 # level 1.2

print("=" * 40)
print("Task 1.2 TRAINS WITH START & END STATIONS")
print("=" * 40)

start = df[df['SN'] == 1][['Train_No', 'Station_Name']].rename(columns={'Station_Name': 'Start_Station'})


end = df.groupby('Train_No').last().reset_index()[['Train_No', 'Station_Name']].rename(columns={'Station_Name': 'End_Station'})

route_summary = pd.merge(start, end, on='Train_No')

print(route_summary)
print("\nTotal Trains Found:", len(route_summary))

# level 1.3

print("=" * 40)
print(" Task 1.3 NUMBER OF STOPS PER TRAIN")
print("=" * 40)

stops_per_train = df.groupby('Train_No')['SN'].max().reset_index()
stops_per_train.columns = ['Train_No', 'Total_Stops']

print(stops_per_train)
print("\nTotal Trains:", len(stops_per_train))

# Level 1.4
print("=" * 40)
print(" Task 1.4 TRAINS WITH MAX & MIN STOPS")
print("=" * 40)
max_stops = stops_per_train.loc[stops_per_train['Total_Stops'].idxmax()]
min_stops = stops_per_train.loc[stops_per_train['Total_Stops'].idxmin()]
print("Train with MOST stops:")
print("  Train No  :", max_stops['Train_No'])
print("  Total Stops:", max_stops['Total_Stops'])

print("\nTrain with LEAST stops:")
print("  Train No  :", min_stops['Train_No'])
print("  Total Stops:", min_stops['Total_Stops'])

#task 1 completed ...



