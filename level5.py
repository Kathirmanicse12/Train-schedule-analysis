import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_dataset.csv")


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

print("=" * 40)
print("TASK 5.1 - PIVOT TABLES")
print("=" * 40)

pivot = df.pivot_table(
    index='Station_Name',
    values='Train_No',
    aggfunc='count'
)
pivot = pivot.sort_values('Train_No', ascending=False)

print("Top 15 Stations - Pivot Table:")
print("=" * 40)
print(pivot.head(15))
print("\nTotal Stations:", len(pivot))

#level 5.2

print("=" * 40)
print("TASK 5.2 - CROSS TABULATIONS")
print("=" * 40)

df_merged = df.merge(journey[['Train_No', 'Route_Type']], 
                     on='Train_No', how='left')

crosstab = pd.crosstab(
    df_merged['Station_Name'],
    df_merged['Route_Type']
)

crosstab['Total'] = crosstab.sum(axis=1)
crosstab = crosstab.sort_values('Total', ascending=False)

print("Top 10 Stations - Cross Tabulation:")
print("=" * 40)
print(crosstab.head(10))
#level 5.3(visulization)
print("=" * 40)
print("TASK 5.3 - CREATING CHARTS")
print("=" * 40)

plt.figure(figsize=(12, 6))
top15 = pivot.head(15)
sns.barplot(x=top15.index, 
            y=top15['Train_No'],
            palette='Blues_r')
plt.title("Top 15 Stations - Train Distribution")
plt.xlabel("Station Name")
plt.ylabel("Number of Trains")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("chart3_pivot.png")
plt.show()
print("Chart 3 Saved! ✅")

plt.figure(figsize=(12, 8))
crosstab_heat = crosstab.drop('Total', axis=1).head(15)
sns.heatmap(crosstab_heat,
            annot=True,
            fmt='d',
            cmap='YlOrRd',
            linewidths=0.5)
plt.title("Station vs Route Type Heatmap")
plt.xlabel("Route Type")
plt.ylabel("Station Name")
plt.tight_layout()
plt.savefig("chart4_heatmap.png")
plt.show()
print("Chart 4 Saved! ✅")

plt.figure(figsize=(8, 8))
route_counts = journey['Route_Type'].value_counts()
plt.pie(route_counts.values,
        labels=route_counts.index,
        autopct='%1.1f%%',
        colors=['green', 'blue', 'red'],
        startangle=90)
plt.title("Route Type Distribution")
plt.savefig("chart5_pie.png")
plt.show()
print("Chart 5 Saved! ✅")
#level 5.4

print("=" * 40)
print("TASK 5.4 - ADVANCED INSIGHTS")
print("=" * 40)

print("1️⃣ Top 3 Busiest Stations:")
top3 = pivot.head(3)
for station, row in top3.iterrows():
    print(f"   {station} : {row['Train_No']} trains")

print("\n2️⃣ Route Type Distribution:")
route_counts = journey['Route_Type'].value_counts()
total = len(journey)
for route, count in route_counts.items():
    percentage = (count / total) * 100
    print(f"   {route} : {count} trains ({percentage:.1f}%)")

print("\n3️⃣ Most Common Route Type:")
crosstab_no_total = crosstab.drop('Total', axis=1)
most_common = crosstab_no_total.idxmax(axis=1)
print(f"   Most stations served by: {most_common.value_counts().index[0]} routes")

print("\n4️⃣ Station with Most Long Routes:")
if 'Long' in crosstab.columns:
    long_station = crosstab['Long'].idxmax()
    long_count = crosstab['Long'].max()
    print(f"   {long_station} : {long_count} long trains")

print("\n5️⃣ Station with Most Short Routes:")
if 'Short' in crosstab.columns:
    short_station = crosstab['Short'].idxmax()
    short_count = crosstab['Short'].max()
    print(f"   {short_station} : {short_count} short trains")

print("=" * 40)
print("LEVEL 5 COMPLETE! ✅")
print("=" * 40)