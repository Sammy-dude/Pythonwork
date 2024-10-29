import json
import time
from http.client import responses

import requests
import unittest

from robot.utils.asserts import assert_equal


class TestAPI(unittest.TestCase):

    def test_get_api(self):
        # Make a GET request to a public API endpoint
        max_response_time = 5  # seconds

        # Measure start time
        start_time = time.time()

        response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/13')

        # Validate the status code
        self.assertEqual(response.status_code, 200, "Status code is not 200")


        # Validate the response content
        json_response = response.json()
        #json_response.repoonetime
        end_time = time.time()
        response_time = end_time - start_time

        # Example assertion on the returned data
        #self.a
        header = response.headers.get("Content-Type")
        assert header.find('application') != -1
        #content_type = response.headers.get("Content-Type")
        print(f"here is the  {header}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8; v=1.0', f"Expected application/json"
        #assert 'Content-Type' in response.headers, "Content-Type header missing"
        #assert response.headers['Content-Type'] == 'application/json', "Content-Type mismatch" + response.headers['Content-Type']
        #assert response.headers['Content-Type'].lower() == 'application/json'
        print(" here is all the respnse " +str(json_response))
        print(json.dumps(json_response, indent=4))

        ousama_dict=json.dumps(json_response)
        ousama_dict1 = json.loads(ousama_dict)

        print(ousama_dict1["title"]== "Activity 13","Title does not match!")
        # json_data_str = json.dumps(json_response, indent=2)
        # json_data = json.load(response.json(), indent=2)
        # print("here is value of the id " + assert_equal(ousama_dict1["title"] == "Activity 13"))
        # print('here is value of the id '+ assert_equal(str(json_data["id"])==13))
# Conditional assertion with printing
        print("Here is the value of the title: " +  ousama_dict1["title"] == "Activity 13")


if __name__ == '__main__':
    unittest.main()
