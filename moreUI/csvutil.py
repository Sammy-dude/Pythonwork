import csv

# Function to read data from the CSV file
def read_test_data():
    data = []
    with open("test_data.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data
print(read_test_data())


def write_test_data(data, output_file):
    # Define the fieldnames (column headers) for the output CSV
    fieldnames = ["username", "password", "expected_result"]
    with open(output_file, "w", newline="") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        csv_writer.writeheader()

        # Write each row of data
        for row in data:
            csv_writer.writerow(row)


# Read data from the original CSV file
data = read_test_data()
print("Read data:", data)

# Write data to a new CSV file
write_test_data(data, "output_test_data.csv")
print("Data written to output_test_data.csv")