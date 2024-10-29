import requests
import json

# Function to fetch data from the API
def fetch_data():
    response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/13")
    return response.json()  # Convert JSON response to Python dictionary

# Function to traverse the JSON data
def traverse_json(data):
    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")

# Function to update and return modified data
def update_data(data):
    if 'title' in data:
        data['title'] = "Updated Title"  # Modify the title field
    return data

# Function to convert dictionary to JSON string
def dict_to_json_string(data):
    return json.dumps(data, indent=4)  # Convert Python dictionary to pretty JSON string

# Main function to execute the operations
def main():
    # Fetch data from API
    data = fetch_data()
    print("Original Data:")
    print(dict_to_json_string(data))

    # Traverse through the original JSON data
    traverse_json(data)

    # Update the data
    updated_data = update_data(data)
    print("Updated Data:")
    print(dict_to_json_string(updated_data))

if __name__ == "__main__":
    main()
