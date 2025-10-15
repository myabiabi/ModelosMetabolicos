import csv

# Define your data or how you'll generate it
data_list = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 24, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"},
]

# Define the CSV file name
csv_filename = "output_data.csv"

# Define the fieldnames (headers)
fieldnames = ["name", "age", "city"]

with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Loop through your data and write each row
    for row_data in data_list:
        writer.writerow(row_data)

print(f"Data saved to {csv_filename}")