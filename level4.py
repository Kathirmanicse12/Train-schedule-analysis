import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_dataset.csv")

print("=" * 40)
print("TASK 4.1 - AVERAGE JOURNEY DURATION")
print("=" * 40)


journey = df.groupby('Train_No')['Distance'].max().reset_index()
journey.columns = ['Train_No', 'Total_Distance_km']

def classify_route(distance):
    if distance < 300:
        return 'Short'
    elif distance < 800:
        return 'Medium'
    else:
        return 'Long'


journey['Route_Type'] = journey['Total_Distance_km'].apply(classify_route)

avg_distance = journey.groupby('Route_Type')['Total_Distance_km'].mean()

print("Average Distance by Route Type:")
print("=" * 40)
print(avg_distance)
#level 4.2
print("=" * 40)
print("TASK 4.2 - HIGH TRAFFIC STATIONS")
print("=" * 40)

station_freq = df.groupby('Station_Name')['Train_No'].nunique().reset_index()
station_freq.columns = ['Station_Name', 'Train_Count']

station_freq = station_freq.sort_values('Train_Count', ascending=False)

top10_stations = station_freq.head(10)

print("Top 10 High Traffic Stations:")
print("=" * 40)
print(top10_stations.to_string(index=False))
print("\nTotal Stations in Dataset:", len(station_freq))

#level 4.3(charts,graphs)
print("=" * 40)
print("TASK 4.3 - CREATING CHARTS")
print("=" * 40)

plt.figure(figsize=(8, 5))
sns.barplot(x=avg_distance.index, 
            y=avg_distance.values,
            palette=['green', 'blue', 'red'])
plt.title("Average Distance by Route Type")
plt.xlabel("Route Type")
plt.ylabel("Average Distance (km)")
plt.savefig("chart1_route_type.png")
plt.show()
print("Chart 1 Saved! ✅")

plt.figure(figsize=(12, 6))
sns.barplot(data=top10_stations,
            x='Station_Name',
            y='Train_Count',
            palette='coolwarm')
plt.title("Top 10 High Traffic Stations")
plt.xlabel("Station Name")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart2_top_stations.png")
plt.show()
print("Chart 2 Saved! ✅")

#level 4.4
print("=" * 40)
print("TASK 4.4 - KEY OBSERVATIONS")
print("=" * 40)

print("1️⃣ Route Type Distribution:")
route_counts = journey['Route_Type'].value_counts()
for route, count in route_counts.items():
    print(f"   {route} Routes : {count} trains")

busiest = station_freq.iloc[0]
print(f"\n2️⃣ Busiest Station:")
print(f"   {busiest['Station_Name']} with {busiest['Train_Count']} trains")

longest = journey.loc[journey['Total_Distance_km'].idxmax()]
print(f"\n3️⃣ Longest Route:")
print(f"   Train No {longest['Train_No']} with {longest['Total_Distance_km']} km")

shortest = journey.loc[journey['Total_Distance_km'].idxmin()]
print(f"\n4️⃣ Shortest Route:")
print(f"   Train No {shortest['Train_No']} with {shortest['Total_Distance_km']} km")

print(f"\n5️⃣ Average Distance Overall:")
print(f"   {journey['Total_Distance_km'].mean():.2f} km")

print("=" * 40)
print("LEVEL 4 COMPLETE! ✅")
print("=" * 40)


