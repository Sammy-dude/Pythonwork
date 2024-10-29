# import json
# import requests
# import unittest
#
# from robot.utils.asserts import assert_equal
#
#
# class TestAPI(unittest.TestCase):
#
#     def test_get_api(self):
#
#
#         response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/13')
#
#         # Validate the status code
#         self.assertEqual(response.status_code, 200, "Status code is not 200")
#
#
#         # Validate the response content
#         json_response = response.json()
#         #json_response.repoonetime
#
#         # Example assertion on the returned data
#         #self.a
#         header = response.headers.get("Content-Type")
#         assert header.find('application') != -1
#         #content_type = response.headers.get("Content-Type")
#         print(f"here is the  {header}")
#         assert response.status_code == 200, f"Expected 200, got {response.status_code}"
#         assert response.headers['Content-Type'] == 'application/json; charset=utf-8; v=1.0', f"Expected application/json"
#         #assert 'Content-Type' in response.headers, "Content-Type header missing"
#         #assert response.headers['Content-Type'] == 'application/json', "Content-Type mismatch" + response.headers['Content-Type']
#         #assert response.headers['Content-Type'].lower() == 'application/json'
#         print(" here is all the respnse " +str(json_response))
#         print(json.dumps(json_response, indent=4))
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()


import requests
import pytest
import json

from typing_extensions import assert_type

# Constants
API_URL = 'https://fakerestapi.azurewebsites.net/api/v1/Activities/13'

for  i in range(1, 11):
    print(i)
# Test 1: Check if the status code is 200
def test_status_code():
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/13')
    count = 0
    while count < 9:
        print("A:) "* count)
        count += 1
    print(f"Status Code on line 62: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print(response.cookies)



# Test 2: Validate the response content-type
def test_content_type():
    response = requests.get(API_URL)
    content_type = response.headers.get('Content-Type')
    json_headers= response.headers.items
    # print(json_headers)
    for key, value in response.headers.items():
        print("\n" +key, value)
        # assert('response.headers.items[key]'=='application/json; charset=utf-8; v=1.0')
    # print("here is the content \n" + response.body())

    assert content_type == 'application/json; charset=utf-8; v=1.0', \
        f"Expected 'application/json; charset=utf-8; v=1.0', got {content_type}"
    # assert json_headers['Server'] == 'Kestrel', "Content-Type is not JSON"
    assert response.headers.get('Server')=='Kestrel', "Content-Type is not JSON"
    assert response.headers.get('Transfer-Encoding') == 'chunked', "Content-Type is not JSON"
    assert response.headers.get('api-supported-versions') == '1.0', "Content-Type is not JSON"
    # Transfer-Encoding chunked
    #
    # api-supported-versions 1.0


# Test 3: Validate the structure of the response JSON
def test_response_json():
    response = requests.get(API_URL)
    json_response = response.json()

    # Check if JSON structure is correct (e.g., expecting 'id' and 'title')
    assert 'id' in json_response, "Key 'id' not found in the response"
    assert 'title' in json_response, "Key 'title' not found in the response"




# Test 4: Check if a specific field has the expected value
def test_specific_field_value5():
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/13')
    json_response = response.json()

    # Example: Check if the 'id' field is equal to 13
    assert json_response['id'] == 13, f"Expected id=13, but got {json_response['id']}"
    assert json_response["completed"] == False, f"Expected false, but got {json_response['completed']}"
    print("\n" ,json_response["completed"])
    # assertFalse.json_response["completed"].

def test_specific_field_value6():
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities')
    json_response = response.json()
    # print(json.dumps(json_response, indent=4))
    # assert json_response
    # for item in json_response:
    # value19= int(json_response['19']);
    print(f"The type of json_response is: {type(json_response)}")
    value19 = json_response[18]['id']
    print(f"The type of json_response is: {type(value19)}")
    print(value19)

    if value19 == 19:
        print(json_response[18]['title'])

        assert str(value19) in json_response[18]['title'], f'Title does not contain "19", title is {json_response[18]['title']} '
    else:
        print(f"ID is {json_response['id']}, no need to assert title contains '19'")
def test_specific_field_value7():
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities')
    json_response = response.json()
    # print(json.dumps(json_response, indent=4))
    # assert json_response
    for item in json_response:
        id_str = str(item["id"])
        tile_str = item["title"]
        print(id_str,tile_str)
        assert id_str in item["title"], f'Title does not contain "19", title is {item["title"]}'

