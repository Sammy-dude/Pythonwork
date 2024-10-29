import json
import pytest

@pytest.mark.asyncio
async def test_activity_api(playwright):
    context = await playwright.request.new_context()
    # Perform a GET request to fetch the activity
    get_response = await context.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/13")
    get_payload = await get_response.json()
    print(await get_response.text())
    print(json.dumps(get_payload, indent=4, sort_keys=True))

    # Assertions for GET request
    assert get_response.status == 200, "Failed to fetch the activity, status code is not 200"
    assert get_payload['id'] == 13, "Activity ID does not match"
    assert 'title' in get_payload, "Title is missing in the activity payload"
    assert get_payload['title'] == 'Activity 13', "Title is missing in the activity payload"
    await context.dispose()
