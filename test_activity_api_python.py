import requests
import json


def test_activity_api():
    try:
        # Perform a GET request to fetch the activity
        get_response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/13")
        get_payload = get_response.json()

        # Assertions for GET request
        assert get_response.status_code == 200, "Failed to fetch the activity, status code is not 200"
        assert get_payload['id'] == 13, "Activity ID does not match"
        assert 'title' in get_payload, "Title is missing in the activity payload"

        print("GET request successful:")
        print(json.dumps(get_payload, indent=4, sort_keys=True))

        # Data for the PUT request
        updated_data = {
            "id": 13,
            "title": "Updated Activity",
            "dueDate": "2024-10-10T00:00:00",
            "completed": False
        }

        # Headers to ensure the request treats the send data as JSON
        headers = {'Content-Type': 'application/json'}

        # Perform a PUT request to update the activity
        put_response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/13", json=updated_data,
                                    headers=headers)
        put_payload = put_response.json()

        # Assertions for PUT request
        assert put_response.status_code == 200, "Failed to update the activity, status code is not 200"
        assert put_payload['title'] == "Updated Activity", "Activity title was not updated correctly"
        assert put_payload['dueDate'] == "2024-10-10T00:00:00", "Due date was not updated correctly"

        print("PUT request successful:")
        print(json.dumps(put_payload, indent=4, sort_keys=True))

    except AssertionError as error:
        print("Assertion Error:", error)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    test_activity_api()
