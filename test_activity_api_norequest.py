import ssl
import urllib.request
import json
from urllib.error import URLError, HTTPError


def test_activity_api_norequest():
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        https_handler = urllib.request.HTTPSHandler(context=context)
        opener = urllib.request.build_opener(https_handler)
        urllib.request.install_opener(opener)

        # Perform a GET request to fetch the activity
        req = urllib.request.Request("https://fakerestapi.azurewebsites.net/api/v1/Activities/13")
        with urllib.request.urlopen(req) as response:
            get_payload = json.loads(response.read().decode())

        # Assertions for GET request
        assert response.status == 200, "Failed to fetch the activity, status code is not 200"
        assert get_payload['id'] == 13, "Activity ID does not match"
        assert 'title' in get_payload, "Title is missing in the activity payload"

        print("GET request successful:")
        print(json.dumps(get_payload, indent=4, sort_keys=True))

        # Data for the PUT request
        updated_data = json.dumps({
            "id": 13,
            "title": "Updated Activity",
            "dueDate": "2024-10-10T00:00:00",
            "completed": False
        }).encode('utf-8')

        # Headers and request setup for PUT
        headers = {
            'Content-Type': 'application/json',
        }
        req = urllib.request.Request("https://fakerestapi.azurewebsites.net/api/v1/Activities/13", data=updated_data,
                                     headers=headers, method='PUT')
        with urllib.request.urlopen(req) as response:
            put_payload = json.loads(response.read().decode())

        # Assertions for PUT request
        assert response.status == 200, "Failed to update the activity, status code is not 200"
        assert put_payload['title'] == "Updated Activity", "Activity title was not updated correctly"
        assert put_payload['dueDate'] == "2024-10-10T00:00:00", "Due date was not updated correctly"

        print("PUT request successful:")
        print(json.dumps(put_payload, indent=4, sort_keys=True))

    except HTTPError as e:
        print('HTTP Error:', e.code, e.reason)
    except URLError as e:
        print('URL Error:', e.reason)
    except Exception as e:
        print('General Error:', e)


if __name__ == "__main__":
    test_activity_api_norequest()
