#level 3.1
import pandas as pd

df = pd.read_csv("Dataset1.csv")

print("=" * 40)
print("TASK 3.1 - HANDLE MISSING VALUES")
print("=" * 40)


print("Missing Values in Each Column:")
print(df.isnull().sum())

df['Arrival_time'].fillna(df['Departure_Time'], inplace=True)


df['Departure_Time'].fillna(df['Arrival_time'], inplace=True)

df.dropna(subset=['Train_No', 'Station_Code'], inplace=True)

print("\nAfter Handling Missing Values:")
print(df.isnull().sum())
print("\nTotal Records Remaining:", len(df))

#level 3.2
print("=" * 40)
print("TASK 3.2 - REMOVE DUPLICATE RECORDS")
print("=" * 40)

print("Total Records Before:", len(df))
print("Duplicate Records Found:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nTotal Records After:", len(df))
print("Duplicate Records Now:", df.duplicated().sum())
print("\nDuplicates Successfully Removed! ✅")
#level 3.3

print("=" * 40)
print("TASK 3.3 - VERIFY STATION ORDER")
print("=" * 40)

def check_order(group):
    sn_list = list(group['SN'])
    return sn_list == sorted(sn_list)


order_check = df.groupby('Train_No').apply(check_order)

correct_trains = order_check[order_check == True].count()
wrong_trains = order_check[order_check == False].count()

print("Trains with CORRECT station order:", correct_trains)
print("Trains with WRONG station order  :", wrong_trains)

if wrong_trains > 0:
    bad_trains = order_check[order_check == False].index.tolist()
    print("\nWrong Order Train Numbers:")
    print(bad_trains)
else:
    print("\nAll trains have correct station order! ✅")
#level 3.4 
print("=" * 40)
print("Task 3.4- SAVE VERIFIED DATA")
print("=" * 40)

df.to_csv("cleaned_dataset.csv", index=False)

print("Dataset saved successfully! ✅")
print("\nFile Name    : cleaned_dataset.csv")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("\nCleaned file saved in your TrainProject folder!")

"import matplotlib; import seaborn; print('Ready! ✅')"