import pandas as pd

df = pd.read_csv("cleaned_dataset.csv")

def find_trains(source, destination):

    source = source.upper().strip()
    destination = destination.upper().strip()
    

    src_trains = set(df[df['Station_Name'].str.upper() 
                    == source]['Train_No'])

    dst_trains = set(df[df['Station_Name'].str.upper() 
                    == destination]['Train_No'])
    
    common_trains = src_trains & dst_trains
    
    if not common_trains:
        print("\ No direct trains found!")
        print(f"   Between {source} and {destination}")
        return
    
    results = []
    for train in common_trains:
        train_df = df[df['Train_No'] == train].sort_values('SN')
        stations = list(train_df['Station_Name'].str.upper())
        
        if source in stations and destination in stations:
            src_idx = stations.index(source)
            dst_idx = stations.index(destination)
            
    
            if src_idx < dst_idx:
                src_row = train_df.iloc[src_idx]
                dst_row = train_df.iloc[dst_idx]
                distance = dst_row['Distance'] - src_row['Distance']
                results.append({
                    'Train_No': train,
                    'Distance_km': distance
                })
    

    if results:
        print("\n" + "=" * 40)
        print(f"🚂 TRAINS FROM {source} TO {destination}")
        print("=" * 40)
        print(f"Total Trains Found: {len(results)}")
        print("-" * 40)
        for r in results:
            print(f"  Train No    : {r['Train_No']}")
            print(f"  Distance    : {r['Distance_km']} km")
            print("-" * 40)
    else:
        print("\n No direct trains found!")
        print(f"   Between {source} and {destination}")

print("=" * 40)
print("🚂 TRAIN ENQUIRY SYSTEM")
print("=" * 40)
print("Type 'exit' anytime to quit!")
print("=" * 40)

while True:
    print()
    source = input("Enter Source Station      : ")
    
    if source.lower() == 'exit':
        print("\nThank you for using Train Enquiry System!")
        print("Goodbye!")
        break
    
    destination = input("Enter Destination Station : ")
    
    if destination.lower() == 'exit':
        print("\nThank you for using Train Enquiry System!")
        print("Goodbye!")
        break
    
    find_trains(source, destination)
    






    

