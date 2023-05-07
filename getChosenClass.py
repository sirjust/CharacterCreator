import requests

def main(className):
    response = requests.get(f'https://dnd5eapi.co/api/classes/{className}')
    # print(response.status_code)  # prints the status code of the response

    apiResponse = response.json()
    return apiResponse